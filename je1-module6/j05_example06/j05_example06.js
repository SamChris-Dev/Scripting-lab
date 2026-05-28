function celsiusToFahrenheit(celsius) {
    return (celsius * 9 / 5) + 32;
}

function fahrenheitToCelsius(fahrenheit) {
    return (fahrenheit - 32) * 5 / 9;
}

function temperatureConverter() {
    let resultDiv = document.getElementById("result");

    let temperature = parseFloat(prompt("Enter temperature: "));

    let typeInput = prompt("Enter conversion type (C or F): ");
    if (typeInput === null) return;

    let type = typeInput.toUpperCase();

    if (isNaN(temperature)) {
        resultDiv.textContent = "Please enter a valid number for temperature.";
        return;
    }

    if (type === "C" || type === "F") {
        let convertedTemp;

        if (type === "C") {
            convertedTemp = celsiusToFahrenheit(temperature);
        } else {
            convertedTemp = fahrenheitToCelsius(temperature);
        }

        let targetUnit = (type === "C" ? "F" : "C");
        resultDiv.textContent = `${temperature}°${type} is equal to ${convertedTemp.toFixed(2)}°${targetUnit}`;
    } else {
        resultDiv.textContent = "Invalid conversion type. Please enter 'C' or 'F'.";
    }
}