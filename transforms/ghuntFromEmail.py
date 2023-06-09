import httpx, trio
from ghunt.apis.peoplepa import PeoplePaHttp
from ghunt.objects.base import GHuntCreds
from ghunt.helpers import gmaps
from maltego_trx.maltego import MaltegoTransform, MaltegoMsg
from maltego_trx.transform import DiscoverableTransform
from extensions import registry

@registry.register_transform(
    display_name="Gmail address to Details [ghunt]", 
    input_entity="maltego.EmailAddress",
    description='Returns details from ghunt results on a given gmail address',
    settings=[],
    output_entities=["maltego.Unknown"]
    )
class ghuntFromEmail(DiscoverableTransform):
    
    @classmethod
    def create_entities(cls, request: MaltegoMsg, response: MaltegoTransform):

        async def main():
            email = request.Value

            ghunt_creds = GHuntCreds()
            ghunt_creds.load_creds(silent=True) # Check creds (but it doesn't crash if they are invalid)

            as_client = httpx.AsyncClient() # Async client

            people_api = PeoplePaHttp(ghunt_creds)
            found, person = await people_api.people_lookup(as_client, email, params_template="max_details")
                                                                            # You can have multiple "params_template" for the GHunt APIs,
                                                                            # for example, on this endpoint, you have "just_gaia_id" by default,
                                                                            # "just_name" or "max_details" which is used in the email CLI module.

            if found:

                # Name
                if "PROFILE" in person.names:
                    name = response.addEntity("maltego.Person", value = person.names["PROFILE"].fullname)
                    name.addProperty("firstname", value = person.names["PROFILE"].firstName)
                    name.addProperty("lastname", value = person.names["PROFILE"].lastName)

                # Profile Photo
                if "PROFILE" in person.profilePhotos:
                    photo = response.addEntity("maltego.Image")
                    photo.addProperty("description", value = person.profilePhotos["PROFILE"].flathash)
                    photo.addProperty("url", value = person.profilePhotos["PROFILE"].url)

                # Enabled applications
                if "PROFILE" in person.inAppReachability:

                    for a in person.inAppReachability["PROFILE"].apps:
                        app = response.addEntity("maltego.Service", value = a)
                        app.addProperty("banner", value = "Google App")

                # Reviews
                err, stats, reviews, photos = await gmaps.get_reviews(as_client, person.personId)
                if reviews:
                    for r in reviews:
                        company = response.addEntity("maltego.Company", value = r.location.name)
                        company.additionalFields.append(["rating", "Rating", '', str(r.rating) + "/5"])
                        company.additionalFields.append(["address", "Address", '', r.location.address])
                        company.additionalFields.append(["type", "Type", '', r.location.types])
                        company.additionalFields.append(["tags", "Tags", '', r.location.tags])
                        company.additionalFields.append(["comment", "Comment", '', r.comment])
                        company.additionalFields.append(["latitude", "Latitude", '', r.location.position.latitude])
                        company.additionalFields.append(["longitude", "Longitude", '', r.location.position.longitude])
            
            # Handle query errors
            else:
                error = response.addEntity("maltego.Phrase")
                error.addProperty("text", value = "Profile not found")

        trio.run(main) # running our async code in a non-async code