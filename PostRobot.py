# -*- coding: utf8 -*-
#python 2.7
#fbconsole:github.com/fbsamples/fbconsole

import fbconsole

def FB_Login():
    fbconsole.AUTH_SUCCESS_HTML = '<h3>Close Window</h3>'
    
    fbconsole.AUTH_SCOPE = ['read_friendlists', 'read_stream', 'publish_checkins', 'publish_actions', 'manage_pages']
    
    fbconsole.authenticate()

              
def FB_Logout():    
    fbconsole.logout()

if __name__=="__main__":
    fb_who = 'me'
    
                
    FB_Login()
    fbconsole.post('/me/feed', {'message':u"小助手上台一鞠躬"})
    #\u5c0f\u52a9\u624b\u4e0a\u53f0\u4e00\u97a0\u8eac
    
    FB_Logout()
    
    print "END"
