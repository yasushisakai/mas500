import mediacloud, json, datetime, ConfigParser, sys

def readArgs() :
	if len(sys.argv) < 2 :
		print "Usage: python compare.py arg <arg2> <arg3> , please add at leaset one word you would like to compare"
		sys.exit(0)
	return' AND '.join(sys.argv[1:])

def readConfigFile() :
	config = ConfigParser.ConfigParser()
	config.read('config.cfg')

	vals = {}

	vals['my_api_key'] = config.get('Media Cloud', 'my_api')
	vals['first_period_start_date'] =  datetime.date(int(config.get('Media Cloud', 'start_year_1')), int(config.get('Media Cloud', 'start_month_1')), int(config.get('Media Cloud', 'start_day_1')))
	vals['first_period_end_date'] =  datetime.date(int(config.get('Media Cloud', 'end_year_1')), int(config.get('Media Cloud', 'end_month_1')), int(config.get('Media Cloud', 'end_day_1')))

	vals['second_period_start_date'] =  datetime.date(int(config.get('Media Cloud', 'start_year_2')), int(config.get('Media Cloud', 'start_month_2')), int(config.get('Media Cloud', 'start_day_2')))
	vals['second_period_end_date'] =  datetime.date(int(config.get('Media Cloud', 'end_year_2')), int(config.get('Media Cloud', 'end_month_2')), int(config.get('Media Cloud', 'end_day_2')))

	vals['year_1'] = config.get('Media Cloud', 'start_year_1')
	vals['year_2'] = config.get('Media Cloud', 'start_year_2')

	vals['media_set_id'] = 'media_sets_id:%s'%config.get('Media Cloud', 'media_set')
	return vals


def callMediaCloudAPI(vals) :
	mc = mediacloud.api.MediaCloud(vals['my_api_key'])

	first_period = mc.sentenceCount(vals['args'], solr_filter=[mc.publish_date_query( vals['first_period_start_date'], vals['first_period_end_date']), vals['media_set_id']])
	second_period = mc.sentenceCount(vals['args'], solr_filter=[mc.publish_date_query( vals['second_period_start_date'], vals['second_period_end_date']), vals['media_set_id']])

	return (first_period, second_period)

def printResults () :
	args = readArgs()
	config_values  = readConfigFile()
	config_values['args'] = args
	periods = callMediaCloudAPI (config_values)
	first_period = periods[0]
	second_period = periods[1]
	year_with_more_mentions = config_values['year_1'] if first_period['count'] > second_period['count'] else config_values['year_2']
	print "%s was mentioned more times in %s" % (args, year_with_more_mentions)
	print "%d mentions in %s, %d mentions in %s"% (first_period['count'], config_values['year_1'], second_period['count'], config_values['year_2'])

if __name__ == "__main__":
    printResults()