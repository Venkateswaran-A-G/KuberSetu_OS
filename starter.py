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
    try:
      with open(filepath,'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
          if row["land_acre"] =="":
            self.display_error_message("Number of Land Acre",row["id"])
            self.offline_queue.append(row)
            continue
          if row["phone"] == "":
            self.display_error_message("Phone Number",row["id"])
            self.offline_queue.append(row)
            continue
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
    except FileNotFoundError:
      print("No Internet. The file is added to offline queue.")
      self.offline_queue.append({"filepath":filepath,"error":"not found"})
      

  def add_member(self,member):
    for i in self.members:
      if i.id == member.id:
        print("WARNING: Duplicate Member Id:",member.id," Found.")
        self.offline_queue.append({"id":member.id,"error":"duplicate"})
        return
    self.members.append(member)

  def dues_report(self):
    total_dues = 0
    for i in self.members:
      total_dues+=i.dues

    return total_dues

  def search_by_crop(self,crop):
    return [m for m in self.members if m.crop.lower() == crop.lower()]

  def filter_consent_verified(self):
    return [m for m in self.members if str(m.consent_otp_verified).lower() == "true"]

  def filter_land_greater_than_2_acres(self):
    return [m for m in self.members if m.land_acre>2]

  def get_crop_category(self,crop):
    return CROP_CATEGORY.get(crop.lower(),"Other")

  def export_clean_json(self, filepath):
    import json
    clean = []
    for m in self.members:
        clean.append({
            "id": m.id,
            "name": m.name,
            "land_acre": m.land_acre,
            "crop": m.crop,
            "phone_hash": hash(m.phone), 
            "join_date": m.join_date,
            "dues": m.dues,
            "consent_otp_verified": m.consent_otp_verified
        })
    with open(filepath, 'w') as f:
      json.dump(clean, f, indent=2)
    print(f"Exported {len(clean)} to {filepath} — bureau input W20")
  def display_error_message(self,fieldName,memberID):
    print("Error:",fieldName," is missing/invalid of id:",memberID)

if __name__ == "__main__":
  import argparse
  parser = argparse.ArgumentParser(prog = 'KuberSetu OS')
  parser.add_argument('--import', dest='import_file', help='Import members.csv')
  parser.add_argument('--import-tally-zip', dest='tally_zip', help='Import Tally zip (offline-first)')
  parser.add_argument('--export', dest='export_file', help='Export clean.json with phone_hash DPDP')
  parser.add_argument('--search', help='Search by crop e.g., ragi')
  parser.add_argument('--filter-land', type=float, help='Filter land > acres e.g., 2')
  parser.add_argument('--dues', action='store_true', help='Show dues report')

  args = parser.parse_args()
  manager = FPOManager()

  if args.import_file:
    manager.load_csv(args.import_file)

  if args.tally_zip:
    manager.load_csv(args.tally_zip)

  if args.search:
    results = manager.search_by_crop(args.search)
    print(f"\n Found {len(results)} farmers with crop {args.search}:")
    for m in results:
      print(f"  {m.id}: {m.name} — {m.land_acre} acre {m.crop}")

  if args.filter_land:
    results = manager.filter_land_greater_than_2_acres()
    filtered = [m for m in manager.members if float(m.land_acre) > args.filter_land]
    print(f"\n Found {len(filtered)} farmers with land > {args.filter_land} acre:")
    for m in filtered:
      print(f"  {m.id}: {m.name} — {m.land_acre} acre")

  if args.dues:
    total = manager.dues_report()
    print(f"\n Dues Report: Total ₹{total}")

  if args.export_file:
    manager.export_clean_json(args.export_file)

  if not any(vars(args).values()):
    print("No args, running demo with members_v2.csv...\n")
    manager.load_csv("members_v2.csv")
    print(f"Loaded {len(manager.members)} members")
    print(f"Search ragi: {len(manager.search_by_crop('ragi'))}")
    print(f"Dues: ₹{manager.dues_report()}")
    manager.export_clean_json("clean.json")

