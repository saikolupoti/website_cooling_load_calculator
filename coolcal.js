function calculateCoolingLoad() {
    const area = parseFloat(document.getElementById("area").value);
    const num_occupants = parseInt(document.getElementById("num_occupants").value);
    const building_type = document.getElementById("building_type").value;
    const outdoor_temp = parseFloat(document.getElementById("outdoor_temp").value);
    const indoor_temp = parseFloat(document.getElementById("indoor_temp").value);

    const coolingLoad = building_type === "residential" ? 100 * num_occupants : 150 * num_occupants;
    const uCoefficient = 30;
    const qConduction = uCoefficient * area * (outdoor_temp - indoor_temp);
    const sensibleCoolingLoad = qConduction + coolingLoad;

    document.getElementById("result").innerText = `The sensible cooling load is: ${sensibleCoolingLoad} W`;
}
