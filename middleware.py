class FacebookMiddleware():
    def process_response(self, request, response):
        response['P3P'] = 'CP="CAO DSP CURa ADMa DEVa TAIa PSAa PSDa IVAi IVDi CONi OUR UNRi OTRi BUS IND PHY ONL UNI COM NAV INT DEM CNT STA PRE GOV LOC"'
        return response

