from eideticker.test import B2GAppActionTest

class Test(B2GAppActionTest):
    def __init__(self, testinfo, appname, **kwargs):
        B2GAppActionTest.__init__(self, testinfo, appname, **kwargs)

        self.cmds = []
        for i in range(20):
            self.cmds.append(['scroll_down'])
