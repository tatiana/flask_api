import logging
import os
import traceback
import unittest

from mock import patch

from venus.utils.middleware import LogMiddleware


class MockContext(object):

    class request(object):
        method = "method"
        url = "url"


class MockApp(object):

    def __init__(self, exception=None):
        self.exception = exception

    class request_context(object):

        def __init__(self, environ):
            return None

        def __enter__(self):
            return MockContext()

        def __exit__(self, type, value, traceback):
            return None

    def full_dispatch_request(self):
        if self.exception is not None:
            raise self.exception
        else:
            return lambda environ, start_response: "%s %s" % (environ, start_response)

    def handle_exception(self, exception):
        pass

    def make_response(self, anything):
        return lambda environ, start_response: "%s %s" % (environ, start_response)


class MockLogger(object):

    def __init__(self):
        self.msg = []

    def error(self, msg):
        self.msg.append(msg)

    def info(self, msg):
        self.msg.append(msg)


class LogTestCase(unittest.TestCase):

    def setUp(self):
        self.original_format_exc = traceback.format_exc

    def tearDown(self):
        traceback.format_exc = self.original_format_exc
        if os.path.exists("test.log"):
            os.remove("test.log")

    def test_middleware_constructor(self):
        middleware = LogMiddleware("app")

        self.assertEquals(middleware.app, "app")
        self.assertTrue(isinstance(middleware.logger, logging.Logger))

    def test_middleware_call_without_exception(self):
        mock_app = MockApp()
        middleware = LogMiddleware(mock_app)
        response = middleware.__call__("something", "else")
        self.assertEquals(response, "something else")

    @patch("traceback.format_exception", return_value="details")
    def test_middleware_call_with_exception(self, mock_traceback):
        mock_app = MockApp(exception=Exception)
        mock_logger = MockLogger()

        middleware = LogMiddleware(mock_app)
        middleware.logger = mock_logger
        response = middleware.__call__("something", "else")

        self.assertEquals(response, "something else")
        self.assertEquals("Request 'url' [method]\ndetails", middleware.logger.msg[0])
