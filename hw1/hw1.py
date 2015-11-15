import mediacloud, json, datetime, ConfigParser

config = ConfigParser.ConfigParser()
config.read('template_config.cfg')

my_api_key = config.get('Media Cloud', 'my_api')
mc = mediacloud.api.MediaCloud(my_api_key)

bees_2013 = mc.sentenceCount('( bee OR bees)', solr_filter=[mc.publish_date_query( datetime.date( 2013, 1, 1), datetime.date( 2014, 1, 1) ), 'media_sets_id:1' ])
bees_2014 = mc.sentenceCount('( bee OR bees)', solr_filter=[mc.publish_date_query( datetime.date( 2014, 1, 1), datetime.date( 2015, 1, 1) ), 'media_sets_id:1' ])

year_with_more_mentions = '2014' if bees_2014['count'] > bees_2013['count'] else '2013'
print "Bees were mentioned more times in %s" % year_with_more_mentions
print "%d mentions in 2014, %d mentions in 2013"% (bees_2014['count'],bees_2013['count'])