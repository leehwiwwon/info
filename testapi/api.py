import requests
from django.http import HttpResponse


def get_wms_map(request):
    wms_endpoint = "http://safemap.go.kr/openApiService/wms/getLayerData.do"

    # Define WMS XML request parameters
    wms_request_xml = """
    <?xml version="1.0" encoding="UTF-8" ?>
    <GetMap>
        <Service>WMS</Service>
        <Version>1.1.1</Version>
        <Request>GetMap</Request>
        <Layers>layer_name</Layers>
        <Styles></Styles>
        <BoundingBox>-180,-90,180,90</BoundingBox>
        <Width>800</Width>
        <Height>400</Height>
        <Format>image/png</Format>
    </GetMap>
    """

    # Construct the WMS request URL
    wms_url = f"{wms_endpoint}?request=GetMap&format=xml&xml={wms_request_xml}"

    # Make the WMS request
    try:
        response = requests.get(wms_url)

        # Check if the request was successful
        if response.status_code == 200:
            # Return the WMS response as the HTTP response
            return HttpResponse(content=response.content, content_type="image/png")
        else:
            return HttpResponse("Error in WMS request", status=response.status_code)
    except requests.RequestException as e:
        return HttpResponse(f"Error: {str(e)}", status=500)
