# PharmsScrape
A script to log onto DISA and pull results from an entered reference number.

ScrapePharms_requests.py file is the one which works currently up to a point where the web server gives a message that the browser doesn't support Java.

PS C:\Users\c1911024\Documents> .\ScrapePharms_requests.py
<html>
 <head>
  <title>
  </title>
  <meta content="no-cache" http-equiv="cache-control"/>
  <meta content="no-cache" http-equiv="pragma"/>
  <noscript>
   <body>
    Your browser does not seem to support JavaScript. Please make sure it is supported and activated
   </body>
  </noscript>
 </head>
</html>


ScrapePharms_requests_html.py is the new project, since requests_html module apparently can support java, but it wants to download Chromium each time I run it, although I have already installed Chromium.  It then just exits after being run.

PS C:\Users\c1911024\Documents> .\ScrapePharms_requests_html.py
[W:pyppeteer.chromium_downloader] start chromium download.
Download may take a few minutes.
Traceback (most recent call last):
  File "C:\Python38\lib\site-packages\urllib3\connection.py", line 156, in _new_conn
    conn = connection.create_connection(
  File "C:\Python38\lib\site-packages\urllib3\util\connection.py", line 84, in create_connection
    raise err
  File "C:\Python38\lib\site-packages\urllib3\util\connection.py", line 74, in create_connection
    sock.connect(sa)
TimeoutError: [WinError 10060] A connection attempt failed because the connected party did not properly respond after a
period of time, or established connection failed because connected host has failed to respond

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Python38\lib\site-packages\urllib3\connectionpool.py", line 665, in urlopen
    httplib_response = self._make_request(
  File "C:\Python38\lib\site-packages\urllib3\connectionpool.py", line 376, in _make_request
    self._validate_conn(conn)
  File "C:\Python38\lib\site-packages\urllib3\connectionpool.py", line 994, in _validate_conn
    conn.connect()
  File "C:\Python38\lib\site-packages\urllib3\connection.py", line 334, in connect
    conn = self._new_conn()
  File "C:\Python38\lib\site-packages\urllib3\connection.py", line 168, in _new_conn
    raise NewConnectionError(
urllib3.exceptions.NewConnectionError: <urllib3.connection.VerifiedHTTPSConnection object at 0x0343A8B0>: Failed to esta
blish a new connection: [WinError 10060] A connection attempt failed because the connected party did not properly respon
d after a period of time, or established connection failed because connected host has failed to respond

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\c1911024\Documents\ScrapePharms_requests_html.py", line 27, in <module>
    r.html.render()  # this call executes the js in the page
  File "C:\Python38\lib\site-packages\requests_html.py", line 586, in render
    self.browser = self.session.browser  # Automatically create a event loop and browser
  File "C:\Python38\lib\site-packages\requests_html.py", line 730, in browser
    self._browser = self.loop.run_until_complete(super().browser)
  File "C:\Python38\lib\asyncio\base_events.py", line 608, in run_until_complete
    return future.result()
  File "C:\Python38\lib\site-packages\requests_html.py", line 714, in browser
    self._browser = await pyppeteer.launch(ignoreHTTPSErrors=not(self.verify), headless=True, args=self.__browser_args)
  File "C:\Python38\lib\site-packages\pyppeteer\launcher.py", line 311, in launch
    return await Launcher(options, **kwargs).launch()
  File "C:\Python38\lib\site-packages\pyppeteer\launcher.py", line 125, in __init__
    download_chromium()
  File "C:\Python38\lib\site-packages\pyppeteer\chromium_downloader.py", line 136, in download_chromium
    extract_zip(download_zip(get_url()), DOWNLOADS_FOLDER / REVISION)
  File "C:\Python38\lib\site-packages\pyppeteer\chromium_downloader.py", line 78, in download_zip
    data = http.request('GET', url, preload_content=False)
  File "C:\Python38\lib\site-packages\urllib3\request.py", line 75, in request
    return self.request_encode_url(
  File "C:\Python38\lib\site-packages\urllib3\request.py", line 97, in request_encode_url
    return self.urlopen(method, url, **extra_kw)
  File "C:\Python38\lib\site-packages\urllib3\poolmanager.py", line 330, in urlopen
    response = conn.urlopen(method, u.request_uri, **kw)
  File "C:\Python38\lib\site-packages\urllib3\connectionpool.py", line 750, in urlopen
    return self.urlopen(
  File "C:\Python38\lib\site-packages\urllib3\connectionpool.py", line 750, in urlopen
    return self.urlopen(
  File "C:\Python38\lib\site-packages\urllib3\connectionpool.py", line 750, in urlopen
    return self.urlopen(
  File "C:\Python38\lib\site-packages\urllib3\connectionpool.py", line 719, in urlopen
    retries = retries.increment(
  File "C:\Python38\lib\site-packages\urllib3\util\retry.py", line 436, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='storage.googleapis.com', port=443): Max retries exceeded wit
h url: /chromium-browser-snapshots/Win/575458/chrome-win32.zip (Caused by NewConnectionError('<urllib3.connection.Verifi
edHTTPSConnection object at 0x0343A8B0>: Failed to establish a new connection: [WinError 10060] A connection attempt fai
led because the connected party did not properly respond after a period of time, or established connection failed becaus
e connected host has failed to respond'))
