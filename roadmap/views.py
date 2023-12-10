from django.shortcuts import render
from django.http import HttpResponse
import requests
import xml.etree.ElementTree as ET
import json


def get_wms_data(request):
    api_key = 'WV0LBMXE-WV0L-WV0L-WV0L-WV0LBMXEFR'
    layer_name = 'A2SM_CRMNLHSPOT_TOT'
    style_name = 'A2SM_CrmnlHspot_Tot_Tot'
    wms_legend_url = f"http://www.safemap.go.kr/legend/legendApiXml.do?apikey={api_key}&layer={layer_name}&style={style_name}"
    try:
        response = requests.get(wms_legend_url)
        if response.status_code == 200:
            xml_data = ET.fromstring(response.content)
            legend_name = xml_data.find(".//NAME").text
            legend_category = xml_data.find(".//CATEGORY").text
            legend_std_date = xml_data.find(".//STDRDE").text
            legend_provider = xml_data.find(".//PROVIDE").text
            legend_warning = xml_data.find(".//WARN").text
            legend_help = xml_data.find(".//HELP").text
            legend_details = []
            features = []
            for item in xml_data.findall(".//item"):
                detail = {
                    'color': item.find("IMG_NM").text,
                    'grade': item.find("LGD_NO").text,
                    'grade_name': item.find("LGD_NM").text,
                    'range': item.find("LGD_RANGE").text,
                }
                legend_details.append(detail)
                feature = {
                    'type': 'Feature',
                    'geometry': {
                        'type': 'Point',
                        'coordinates': [
                            float(item.find("LGD_RANGE").text) if item.find("LGD_RANGE") is not None and item.find(
                                "LGD_RANGE").text is not None else 0.0,
                            float(item.find("LGD_RANGE").text) if item.find("LGD_RANGE") is not None and item.find(
                                "LGD_RANGE").text is not None else 0.0,
                        ],

                    },
                    'properties': {
                        'color': item.find("IMG_NM").text,
                        'grade': item.find("LGD_NO").text,
                        'grade_name': item.find("LGD_NM").text,
                    },
                }
                features.append(feature)

            geojson_data = {
                'type': 'FeatureCollection',
                'features': features,
            }
            geojson_string = json.dumps(geojson_data)
            return render(request, 'api.html', {
                'legend_name': legend_name,
                'legend_category': legend_category,
                'legend_std_date': legend_std_date,
                'legend_provider': legend_provider,
                'legend_warning': legend_warning,
                'legend_help': legend_help,
                'legend_details': legend_details,
                'geojson_data': geojson_string,
            })
        else:
            return HttpResponse("Error in WMS legend request", status=response.status_code)
    except requests.RequestException as e:
        return HttpResponse(f"Error: {str(e)}", status=500)
