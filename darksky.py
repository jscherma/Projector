import forecastio

api_key = "4050ffebe03afd73bbd6cc56d063781c"
lat = 40.7128
lng = -74.0060

forecast = forecastio.load_forecast("4050ffebe03afd73bbd6cc56d063781c", 40.7128, -74.0060)

forecast.update()

print "============Current Data============"
by_current = forecast.currently()
print "Currently: %s and %s degrees" % (by_current.summary, by_current.temperature)

print "============Hourly Data============"
byHour = forecast.hourly()
print "Hourly Summary: %s" % (byHour.summary)
print byHour.icon

for hourlyData in byHour.data:
    print hourlyData.temperature


print "============Daily Data============"

print forecast.daily()
