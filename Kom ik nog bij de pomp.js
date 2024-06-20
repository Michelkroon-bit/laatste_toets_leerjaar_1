// Je was aan het kamperen met je vrienden ver weg van huis, maar als het tijd is om terug te gaan, realiseer je je dat je brandstof bijna op is en het dichtstbijzijnde tankstation is 80 kilometer verderop! Je weet dat je auto gemiddeld ongeveer 10 kilometer per liter rijdt. Je hebt nog 8 liter over.

// Schrijf een functie die je vertelt of het mogelijk is om bij het tankstation te komen of niet.

// De functie moet true teruggeven als het mogelijk is en false als dat niet zo is


// Maak de volgende JS functie af:
function kanBereikenTankstation(kilometersNaarTankstation, kilometersPerLiter, resterendeLiters) {
    
    aantal_liters_over = resterendeLiters *  kilometersPerLiter;
    totaal = aantal_liters_over - kilometersNaarTankstation;

    if(totaal <0){ 
        return false;}
    if(totaal >=0){
        return true;
    }
    
}


document.getElementById('Test1').innerHTML = `Test 1: ${kanBereikenTankstation(80, 10, 10)}parameters used (80 km tot tankstation , 10 km per liter , 10 liter(s) over)`;
document.getElementById('Test2').innerHTML = `Test 2: ${kanBereikenTankstation(50, 10, 8)} parameters used (50 km tot tankstation , 10 km per liter , 8 liter(s) over)`;
document.getElementById('Test3').innerHTML = `Test 3: ${kanBereikenTankstation(43, 10, 3)} parameters used (43 km tot tankstation , 10 km per liter , 3 liter(s) over)`;
document.getElementById('Test4').innerHTML = `Test 4: ${kanBereikenTankstation(53, 10, 8)} parameters used (53 km tot tankstation , 10 km per liter , 8 liter(s) over)`;
document.getElementById('Test5').innerHTML = `Test 5: ${kanBereikenTankstation(81, 10, 2)} parameters used (81 km tot tankstation , 10 km per liter , 2 liter(s) over)`;
document.getElementById('Test6').innerHTML = `Test 6: ${kanBereikenTankstation(100, 10, 10)} parameters used   (100 km tot tankstation , 10 km per liter , 10 liter(s)over)`;
document.getElementById('Test7').innerHTML = `Test 7: ${kanBereikenTankstation(122, 10, 9)} parameters used  (122 km tot tankstation , 10 km per liter , 9 liter(s) over)`;
document.getElementById('Test8').innerHTML = `Test 8: ${kanBereikenTankstation(103, 10, 7)} parameters used  (103 km tot tankstation , 10 km per liter , 7 liter(s) over)`;

