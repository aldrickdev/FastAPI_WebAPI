import requests

def main():

  choice :str = input("[R]eport weather or [S]ee reports:\t")
  while choice:
    if choice.lower().strip() == 'r':
      report_event()
    elif choice.lower().strip() == 's':
      see_events()
    else:
      print(f"Dont know what to do with {choice}")

    choice :str = input("[R]eport weather or [S]ee reports:\t")

def report_event():
  url = "http://127.0.0.1:8001/api/reports"
  desc = input("Whats going on:  ")
  city = input("In what city:  ")
  data = {
    "desc": desc,
    "loc": {
      "city": city,
    },
  }
  resp = requests.post(url, json=data)
  resp.raise_for_status()
  result = resp.json()
  print(f"Reported new Event: {result.get('id')} ")

def see_events():
  url = "http://127.0.0.1:8001/api/reports"
  resp = requests.get(url)
  resp.raise_for_status() 

  data = resp.json()
  for report in data:
    print(f"{report.get('loc').get('city')} has {report.get('desc')}")
  

if __name__ == '__main__':
  main()