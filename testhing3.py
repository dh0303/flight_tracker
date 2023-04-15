from amadeus import Client, ResponseError

amadeus = Client(
    client_id='XgxDwEAknQAEA0YVcGZW8MNoG8ZyTBBX',
    client_secret='eBQCujYHCw79WFpK'
)

try:
    response = amadeus.shopping.flight_offers_search.get(
        originLocationCode='MAD',
        destinationLocationCode='ATH',
        departureDate='2023-11-01',
        adults=1)
    print(response.data)

    f = open("flightTest.txt", "w")
    f.write(str(response.data))
    f.close()

    
except ResponseError as error:
    print(error)