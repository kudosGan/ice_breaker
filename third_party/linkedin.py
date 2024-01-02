import  os

import requests


new*
def scape_linkedin_profile(linkedin_profile_url:str):
    """ scarpe informtion from LinkedIn profles,
    Manually scarpe the information from the linkedin pofile """

    api_endpoint ="https://nubela.co/proxycurl/api/v2/linkedin"
    header_dic = {"Aurhorization": f'bearer {os.environ.get("PROXYCURL_API_KEY")}'}


    response =requests.get(
        api_endpoint, params={"url": linkedin_profile_url},headers=header_dic
        
    )


    pass

