import requests
from django.http import HttpResponse

def get_wms_legend(request):
    # Replace 'your_api_key' with your actual API key
    api_key = 'WV0LBMXE-WV0L-WV0L-WV0L-WV0LBMXEFR'
    layer_name = 'A2SM_CRMNLHSPOT_TOT'
    style_name = 'A2SM_CrmnlHspot_Tot_Tot'

    # Construct the WMS legend request URL
    wms_legend_url = f"http://www.safemap.go.kr/legend/legendApiXml.do?apikey={api_key}&layer={layer_name}&style={style_name}"

    # Make the WMS legend request
    try:
        response = requests.get(wms_legend_url)

        # Check if the request was successful
        if response.status_code == 200:
            # Return the legend response as the HTTP response
            return HttpResponse(content=response.content, content_type="application/xml")
        else:
            return HttpResponse("Error in WMS legend request", status=response.status_code)
    except requests.RequestException as e:
        return HttpResponse(f"Error: {str(e)}", status=500)
