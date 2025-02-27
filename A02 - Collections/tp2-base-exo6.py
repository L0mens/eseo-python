import requests 

def get_university_data(country = "France"):
    url = f"http://universities.hipolabs.com/search?country={country}"

    rawdata = requests.get(url)

    if not rawdata:
        raise Exception

    data = rawdata.json()
    return data


if __name__ == "__main__":
    uni_data = get_university_data("France")
    print(uni_data)