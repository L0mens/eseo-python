import requests 
from operator import itemgetter

def get_university_data(country = "France"):
    url = f"http://universities.hipolabs.com/search?country={country}"

    rawdata = requests.get(url)

    if not rawdata:
        raise Exception

    data = rawdata.json()
    return data


if __name__ == "__main__":
    uni_data = get_university_data("United+States")
    uni_with_state = [x for x in uni_data if x.get("state-province", None)]
    uni_sorted = sorted(uni_with_state, key=itemgetter('state-province')) 
    for universite in uni_sorted:
        print(f"{universite.get('name')} : {universite.get('state-province')}")
