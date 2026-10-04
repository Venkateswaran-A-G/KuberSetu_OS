import os, json, pytest
from starter import FPOMember, FPOManager, CROP_CATEGORY

@pytest.fixture
def manager():
    m = FPOManager()
    m.load_csv("members_v2.csv")
    return m

def test_load_csv_and_count(manager):
    # Task 2: load 8 members
    assert len(manager.members) == 8
    assert len(manager.offline_queue) == 0

def test_search_by_crop_and_category(manager):
    ragi = manager.search_by_crop("ragi")
    assert len(ragi) == 3
    assert len(manager.search_by_crop("RAGI")) == 3
    assert manager.get_crop_category("ragi") == "Millets"
    assert manager.get_crop_category("RAGI") == "Millets"
    assert manager.get_crop_category("paddy") == "Cereals"
    assert manager.get_crop_category("tomato") == "Other"
    assert CROP_CATEGORY == {'ragi':'Millets','paddy':'Cereals','maize':'Cereals'}

def test_filter_land_and_consent(manager):

    land_gt2 = manager.filter_land_greater_than_2_acres()
    assert len(land_gt2) == 4
    assert all(float(m.land_acre) > 2 for m in land_gt2)
    
    consent = manager.filter_consent_verified()
    assert len(consent) == 6  

def test_dues_report_and_export():
    m = FPOManager()
    m.load_csv("members_v2.csv")
    total = m.dues_report()
    assert total == 3000.0  
    
    
    m.export_clean_json("test_clean.json")
    assert os.path.exists("test_clean.json")
    with open("test_clean.json") as f:
        data = json.load(f)
    assert len(data) == 8
    assert "phone_hash" in data[0]
    assert "phone" not in data[0] 
    assert "crop_category" in data[0]
    os.remove("test_clean.json")

def test_offline_queue_and_duplicate_and_notfound():

    m = FPOManager()
    m.load_csv("dirty.csv")
    assert len(m.members) == 2
    assert len(m.offline_queue) == 2
    assert isinstance(m.offline_queue[0], dict)  
    assert "name" in m.offline_queue[0]

    m2 = FPOManager()
    m2.load_csv("notfound.csv")
    assert len(m2.members) == 0
    assert len(m2.offline_queue) == 1
    assert m2.offline_queue[0]["error"] == "not found"

    m3 = FPOManager()
    m3.load_csv("members_v2.csv")
    dup = FPOMember(1, "Duplicate", 1.0, "ragi", "99999xxxxx", "2024-01-01", 0, "True")
    m3.add_member(dup)
    assert len(m3.members) == 8  
    assert len(m3.offline_queue) == 1
    assert m3.offline_queue[0]["error"] == "duplicate"
    assert isinstance(m3.offline_queue[0], dict)
