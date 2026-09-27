class FPOMember:
  def __init__(self,id, name, land_acre, crop, phone, join_date,dues,consent_otp_verified):
    self.id = id
    self.name = name
    self.land_acre = land_acre
    self.crop = crop
    self.phone = phone
    self.join_date = join_date
    self.dues = dues
    self.consent_otp_verified = consent_otp_verified

CROP_CATEGORY = {
    'ragi': 'Millets',
    'paddy': 'Cereals',
    'maize': 'Cereals'
}
    
class FPOManager:
  def __init__(self):
    self.members = []
    self.offline_queue = []

  def load_csv(self, filepath):
    import csv 
    with open(filepath,'r') as file:
      reader = csv.DictReader(file)
      for row in reader:
        m = FPOMember(
          int(row["id"]),
          row["name"],
          float(row["land_acre"]),
          row['crop'],
          row["phone"],
          row["join_date"],
          float(row["dues"]),
          row["consent_otp_verified"]
          )
        self.add_member(m)

  def add_member(self,member):
    for i in self.members:
      if i.id == member.id:
        print("WARNING: Duplicate Member Id:",member.id," Found.")
        return
    self.members.append(member)

  def dues_report(self):
    total_dues = 0
    for i in self.members:
      total_dues+=i.dues

    return total_dues

  def search_by_crop(self,crop):
    return [m for m in self.members if m.crop == crop]

  def filter_consent_verified(self):
    return [m for m in self.members if m.consent_otp_verified == "True"]

  def filter_land_greater_than_2_acres(self):
    return [m for m in self.members if m.land_acre>2]

  def get_crop_category(self,crop):
    return CROP_CATEGORY.get(crop.lower(),"Other")