'''
 ***********************************************************
 * Outlaw Add-on
 *
 * @package plugin.video.outlaw
 *
 * @copyright (c) 2021, Outlaw
 * @license GNU General Public License, version 3 (GPL-3.0)
 *
 ***********************************************************
'''

#CM - 06/24/2021
import xbmc

from resources.lib.modules import control
from resources.lib.modules import log_utils

control.execute('RunPlugin(plugin://%s)' % control.get_plugin_url({'action': 'service'}))
def syncTraktLibrary():
    control.execute('RunPlugin(plugin://%s)' % 'plugin.video.outlaw/?action=tvshowsToLibrarySilent&url=traktcollection')
    control.execute('RunPlugin(plugin://%s)' % 'plugin.video.outlaw/?action=moviesToLibrarySilent&url=traktcollection')


if control.setting('autoTraktOnStart') == 'true':
    syncTraktLibrary()

if int(control.setting('schedTraktTime')) > 0:
    log_utils.log('###############################################################', log_utils.LOGNOTICE)
    log_utils.log('#################### STARTING TRAKT SCHEDULING ################', log_utils.LOGNOTICE)
    log_utils.log('#################### SCHEDULED TIME FRAME ' + control.setting('schedTraktTime') + ' HOURS ################', log_utils.LOGNOTICE)
    timeout = 3600 * int(control.setting('schedTraktTime'))

    monitor = xbmc.Monitor()
    while not monitor.abortRequested():
        try:
            monitor.waitForAbort(timeout)
            syncTraktLibrary()
        except:
            pass
        finally:
            del monitor
