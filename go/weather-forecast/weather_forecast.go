// Package weather tell the forecast.
package weather

// CurrentCondition tracks the current condition.
var CurrentCondition string

// CurrentLocation tracks the current location.
var CurrentLocation string

// Forecast returns a string with the formated weather forecast.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
