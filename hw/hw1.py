import mediacloud, json, datetime, ConfigParser
import logging

config = ConfigParser.ConfigParser()
#config.read('template_config.cfg') #intentional mistake for test test.py
config.read('config.cfg')

my_api_key = config.get('Media Cloud', 'my_api')


# function for unit testing
def connect_to_media_cloud(_api_token):
    logger = logging.getLogger(__name__)
    mc = mediacloud.api.MediaCloud(_api_token)

    if not mc.verifyAuthToken():
        logger.error('token authentication failed')
        return None

        logger.debug('token authentication success')

    return mc


if __name__ == '__main__':

    #where is the right place to initiate logging????
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    handler = logging.FileHandler('test.log')
    handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)


    logger.info('*start***********************************************')
    mc = connect_to_media_cloud(my_api_key)

    logger.debug(str(mc))


    bees_2013 = mc.sentenceCount('( bee OR bees)', solr_filter=[mc.publish_date_query( datetime.date( 2013, 1, 1), datetime.date( 2014, 1, 1) ), 'media_sets_id:1' ])
    bees_2014 = mc.sentenceCount('( bee OR bees)', solr_filter=[mc.publish_date_query( datetime.date( 2014, 1, 1), datetime.date( 2015, 1, 1) ), 'media_sets_id:1' ])

    year_with_more_mentions = '2014' if bees_2014['count'] > bees_2013['count'] else '2013'
    print "Bees were mentioned more times in %s" % year_with_more_mentions
    print "%d mentions in 2014, %d mentions in 2013"% (bees_2014['count'],bees_2013['count'])
    logger.info('*end**********************************************')
