import requests
import time

class AudibleSession:

    @staticmethod
    def current_milli_time():
        return int(round(time.time() * 1000))

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.HOSTS = dict(
            amazon_login = "www.amazon.com",
            amazon_api = "api.amazon.com",
            audible_api = "api.audible.com",
        )
        self.endpoints = dict(
            oauth_url="/ap/signin?openid.oa2.response_type=token&openid.return_to=https://www.amazon.com/ap/maplanding&openid.assoc_handle=amzn_audible_ios_us&openid.identity=http://specs.openid.net/auth/2.0/identifier_select&pageId=amzn_audible_ios&accountStatusPolicy=P1&openid.claimed_id=http://specs.openid.net/auth/2.0/identifier_select&openid.mode=checkid_setup&openid.ns.oa2=http://www.amazon.com/ap/ext/oauth/2&openid.oa2.client_id=device:6a52316c62706d53427a5735505a76477a45375959566674327959465a6374424a53497069546d45234132435a4a5a474c4b324a4a564d&language=en_US&openid.ns.pape=http://specs.openid.net/extensions/pape/1.0&marketPlaceId=AF2M0KC94RCEA&openid.oa2.scope=device_auth_access&forceMobileLayout=true&openid.ns=http://specs.openid.net/auth/2.0&openid.pape.max_auth_age=0"

        )

        headers = dict()

        headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
        headers["Accept-Charset"] = "utf-8"
        headers["Accept-Language"] = "en-US"
        headers["Host"] = "www.amazon.com"
        headers["Origin"] = "https://www.amazon.com"
        headers["User-Agent"] = "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Mobile/14E304"


        metadata1 = '{"start":' + self.current_milli_time()  + ',"interaction":{"keys":0,"keyPressTimeIntervals":[],"copies":0,"cuts":0,"pastes":0,"clicks":0,"touches":0,"mouseClickPositions":[],"keyCycles":[],"mouseCycles":[],"touchCycles":[]},"version":"3.0.0","lsUbid":"X39-6721012-8795219:1549849158","timeZone":-6,"scripts":{"dynamicUrls":["https://images-na.ssl-images-amazon.com/images/I/61HHaoAEflL._RC|11-BZEJ8lnL.js,01qkmZhGmAL.js,71qOHv6nKaL.js_.js?AUIClients/AudibleiOSMobileWhiteAuthSkin#mobile","https://images-na.ssl-images-amazon.com/images/I/21T7I7qVEeL._RC|21T1XtqIBZL.js,21WEJWRAQlL.js,31DwnWh8lFL.js,21VKEfzET-L.js,01fHQhWQYWL.js,51TfwrUQAQL.js_.js?AUIClients/AuthenticationPortalAssets#mobile","https://images-na.ssl-images-amazon.com/images/I/0173Lf6yxEL.js?AUIClients/AuthenticationPortalInlineAssets","https://images-na.ssl-images-amazon.com/images/I/211S6hvLW6L.js?AUIClients/CVFAssets","https://images-na.ssl-images-amazon.com/images/G/01/x-locale/common/login/fwcim._CB454428048_.js"],"inlineHashes":[-1746719145,1334687281,-314038750,1184642547,-137736901,318224283,585973559,1103694443,11288800,-1611905557,1800521327,-1171760960,-898892073],"elapsed":52,"dynamicUrlCount":5,"inlineHashesCount":13},"plugins":"unknown||320-568-548-32-*-*-*","dupedPlugins":"unknown||320-568-548-32-*-*-*","screenInfo":"320-568-548-32-*-*-*","capabilities":{"js":{"audio":true,"geolocation":true,"localStorage":"supported","touch":true,"video":true,"webWorker":true},"css":{"textShadow":true,"textStroke":true,"boxShadow":true,"borderRadius":true,"borderImage":true,"opacity":true,"transform":true,"transition":true},"elapsed":1},"referrer":"","userAgent":"' + headers['user-agent'] + '","location":"https://www.amazon.com' + self.endpoints['oath_url'] + '","webDriver":null,"history":{"length":1},"gpu":{"vendor":"Apple Inc.","model":"Apple A9 GPU","extensions":[]},"math":{"tan":"-1.4214488238747243","sin":"0.8178819121159085","cos":"-0.5753861119575491"},"performance":{"timing":{"navigationStart":' + ' + self.current_milli_time() + ' + ',"unloadEventStart":0,"unloadEventEnd":0,"redirectStart":0,"redirectEnd":0,"fetchStart":' + self.current_milli_time() + ',"domainLookupStart":' + self.current_milli_time() + ',"domainLookupEnd":' + self.current_milli_time() + ',"connectStart":' + self.current_milli_time() + ',"connectEnd":' + self.current_milli_time() + ',"secureConnectionStart":' + self.current_milli_time() + ',"requestStart":' + self.current_milli_time() + ',"responseStart":' + self.current_milli_time() + ',"responseEnd":' + self.current_milli_time() + ',"domLoading":' + self.current_milli_time() + ',"domInteractive":' + self.current_milli_time() + ',"domContentLoadedEventStart":' + self.current_milli_time() + ',"domContentLoadedEventEnd":' + self.current_milli_time() + ',"domComplete":' + self.current_milli_time() + ',"loadEventStart":' + self.current_milli_time() + ',"loadEventEnd":' + self.current_milli_time() + '}},"end":' + self.current_milli_time() + ',"timeToSubmit":108873,"form":{"email":{"keys":0,"keyPressTimeIntervals":[],"copies":0,"cuts":0,"pastes":0,"clicks":0,"touches":0,"mouseClickPositions":[],"keyCycles":[],"mouseCycles":[],"touchCycles":[],"width":290,"height":43,"checksum":"C860E86B","time":12773,"autocomplete":false,"prefilled":false},"password":{"keys":0,"keyPressTimeIntervals":[],"copies":0,"cuts":0,"pastes":0,"clicks":0,"touches":0,"mouseClickPositions":[],"keyCycles":[],"mouseCycles":[],"touchCycles":[],"width":290,"height":43,"time":10353,"autocomplete":false,"prefilled":false}},"canvas":{"hash":-373378155,"emailHash":-1447130560,"histogramBins":[]},"token":null,"errors":[],"metrics":[{"n":"fwcim-mercury-collector","t":0},{"n":"fwcim-instant-collector","t":0},{"n":"fwcim-element-telemetry-collector","t":2},{"n":"fwcim-script-version-collector","t":0},{"n":"fwcim-local-storage-identifier-collector","t":0},{"n":"fwcim-timezone-collector","t":0},{"n":"fwcim-script-collector","t":1},{"n":"fwcim-plugin-collector","t":0},{"n":"fwcim-capability-collector","t":1},{"n":"fwcim-browser-collector","t":0},{"n":"fwcim-history-collector","t":0},{"n":"fwcim-gpu-collector","t":1},{"n":"fwcim-battery-collector","t":0},{"n":"fwcim-dnt-collector","t":0},{"n":"fwcim-math-fingerprint-collector","t":0},{"n":"fwcim-performance-collector","t":0},{"n":"fwcim-timer-collector","t":0},{"n":"fwcim-time-to-submit-collector","t":0},{"n":"fwcim-form-input-telemetry-collector","t":4},{"n":"fwcim-canvas-collector","t":2},{"n":"fwcim-captcha-telemetry-collector","t":0},{"n":"fwcim-proof-of-work-collector","t":1},{"n":"fwcim-ubf-collector","t":0},{"n":"fwcim-timer-collector","t":0}]}'
