from api.amsterdam_api import AmsterdamApi
from api.ns_api import NSApi

def trash_bins():
    amsterdam_api = AmsterdamApi()
    list_trash_bins = amsterdam_api.get_trash_bins()

    print("Overview of trash bins in Amsterdam")

    for trash_bin in list_trash_bins:
        print(
            str(trash_bin['id']) + "\t" +
            trash_bin['name'] + "\t" +
            trash_bin['type'] + "\t" +
            trash_bin['address']
        )


def main():
    print("NS API Test")
    ns_api = NSApi()

    totaltrainstation = len(ns_api.get_train_stations())
    totaldisruptions = ns_api.get_disruptionstotal()
    disrperc = (round(totaldisruptions / totaltrainstation * 100))
    print("the percentage of disruptions is currently", disrperc, "%")
    print(ns_api.get_disruptiontop3())


    # Get a list of disruptions
    #print(ns_api.get_disruptions())

    # Get all the departure trains from one train station (direction and delay in seconds)
    # Use id from get_train_stations() as identifier.
    #print(ns_api.get_departures("8400057"))


if __name__ == "__main__":
    main()
