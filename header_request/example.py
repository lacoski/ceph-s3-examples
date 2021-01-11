from rgwadmin import RGWAdmin

ACCESS_KEY = 'AAT30ADPPNWA0FSLMAPJ'
SECRET_KEY = '7D3fgmOoCzix6qwe3KM2DmbSmaWGDZbCH4jBHqiO'

rgw = RGWAdmin(access_key=ACCESS_KEY, secret_key=SECRET_KEY, server='172.16.70.31:7480', secure=False)
rgw.get_users()