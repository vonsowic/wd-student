u"""
A web crawler which log in to dziekanat.agh.edu.pl and give you your grades
"""
from requests import session
from parser import getMarksTable


class WdCrawler:

    def __init__(self, login, password, url="https://dziekanat.agh.edu.pl"):
        self.login = login
        self.password = password
        self.url = url

    def loginToWD(self):
        u"""log in to server"""
        login_data = self.getLoginData()
        sess = session().post(self.url+"/Logowanie2.aspx", data=login_data)
        return sess

    def getFinalMarks(self):
        with session() as c:
            c.post('https://dziekanat.agh.edu.pl/Logowanie2.aspx', data=self.getLoginData())
            res = c.get('https://dziekanat.agh.edu.pl/OcenyP.aspx')
        return res.text

    def getLoginData(self):
        # TODO: make form(login_data) to load itself automatically
        login_data = {
            "ctl00_ctl00_ScriptManager1_HiddenField": "",
            "__EVENTTARGET": "",
            "__EVENTARGUMENT": "",
            "__VIEWSTATE": "/wEPDwUKMTc3NTQ1OTc2NA8WAh4DaGFzZRYCZg9kFgJmD2QWAgIBD2QWBAICD2QWAgIBD2QWAgIBD2QWAgICDxQrAAIUKwACDxYEHgtfIURhdGFCb3VuZGceF0VuYWJsZUFqYXhTa2luUmVuZGVyaW5naGQPFCsAARQrAAIPFggeBFRleHQFHVd5c3p1a2l3YXJrYSBwb2R6aWHFgnUgZ29kemluHgtOYXZpZ2F0ZVVybAUTL1BvZHpHb2R6aW5Ub2suYXNweB4FVmFsdWUFHVd5c3p1a2l3YXJrYSBwb2R6aWHFgnUgZ29kemluHgdUb29sVGlwBR1XeXN6dWtpd2Fya2EgcG9kemlhxYJ1IGdvZHppbmRkDxQrAQFmFgEFdFRlbGVyaWsuV2ViLlVJLlJhZE1lbnVJdGVtLCBUZWxlcmlrLldlYi5VSSwgVmVyc2lvbj0yMDEyLjMuMTIwNS4zNSwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj0xMjFmYWU3ODE2NWJhM2Q0ZBYCZg8PFggfAwUdV3lzenVraXdhcmthIHBvZHppYcWCdSBnb2R6aW4fBAUTL1BvZHpHb2R6aW5Ub2suYXNweB8FBR1XeXN6dWtpd2Fya2EgcG9kemlhxYJ1IGdvZHppbh8GBR1XeXN6dWtpd2Fya2EgcG9kemlhxYJ1IGdvZHppbmRkAgQPZBYCAgMPZBYSAgEPFgIeCWlubmVyaHRtbAUtV2lydHVhbG5hIFVjemVsbmlhPCEtLSBzdGF0dXM6IDI3MTA1Njc5MCAtLT4gZAINDw8WAh4ETW9kZQsqJVN5c3RlbS5XZWIuVUkuV2ViQ29udHJvbHMuVGV4dEJveE1vZGUCZGQCFQ8PFgIfAwUZT2R6eXNraXdhbmllIGhhc8WCYTxiciAvPmRkAhcPZBYCAgMPEGQPFgJmAgEWAgUHc3R1ZGVudAUIZHlkYWt0eWsWAWZkAhkPZBYEAgEPDxYCHwMFNDxiciAvPkx1YiB6YWxvZ3VqIHNpxJkgamFrbyBzdHVkZW50IHByemV6IE9mZmljZTM2NTpkZAIDDw8WAh8DBQhQcnplamTFumRkAhsPDxYEHwMFGFNlcndpcyBBYnNvbHdlbnTDs3c8YnIvPh4HVmlzaWJsZWhkZAIfDw8WAh8JaGRkAiEPDxYCHwloZBYGAgEPDxYCHwNkZGQCAw8PFgIfAwUGQW51bHVqZGQCBQ8PFgIfAwUHUG9iaWVyemRkAiMPDxYCHwMFI1fFgsSFY3ogcmVrbGFtxJkgYXBsaWthY2ppIG1vYmlsbmVqZGQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgEFSmN0bDAwJGN0bDAwJFRvcE1lbnVQbGFjZUhvbGRlciRUb3BNZW51Q29udGVudFBsYWNlSG9sZGVyJE1lbnVUb3AzJG1lbnVUb3AzOrIq3F+MeLi7YxUj2khaBeFDseU=",
            "__VIEWSTATEGENERATOR": "BBDE9B47",
            "ctl00_ctl00_TopMenuPlaceHolder_TopMenuContentPlaceHolder_MenuTop3_menuTop3_ClientState": "",
            "ctl00$ctl00$ContentPlaceHolder$MiddleContentPlaceHolder$txtIdent": self.login,
            "ctl00$ctl00$ContentPlaceHolder$MiddleContentPlaceHolder$txtHaslo": self.password,
            "ctl00$ctl00$ContentPlaceHolder$MiddleContentPlaceHolder$butLoguj": "Zaloguj",
            "ctl00$ctl00$ContentPlaceHolder$MiddleContentPlaceHolder$rbKto": "student"
        }
        return login_data

    def getMarksInHtmlTable(self):
        return getMarksTable(self.getFinalMarks())

if __name__ == "__main__":
    crawler = WdCrawler("login", "haslo")
    response = crawler.getMarksInHtmlTable()
    print(response)
    f = open("test.html", "w")
    f.write(response)
    f.close()

