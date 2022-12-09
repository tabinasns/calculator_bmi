// perhitungan bmi
function bmi(){
    var brt = parseFloat(document.getElementById("berat").value);
    var tng = parseFloat(document.getElementById("tinggi").value)/100;

    var hasil = brt / (tng*tng);
    var air = brt * 30;

    if (hasil < 17.0){
        keterangan = "Kurus, Kekurangan berat badan tingkat berat";
    }
    else if ((hasil >= 17.0) & (hasil <= 18.4)){
        keterangan = "Kurus, Kekurangan berat badan tingkat ringan";
    }
    else if ((hasil >= 18.5) & (hasil <= 25.0)){
        keterangan = "Normal";
    }
    else if ((hasil >= 25.1) & (hasil <= 27.0)){
        keterangan = "Gemuk, Kelebihan berat badan tingkat ringan";
    }
    else{
        keterangan = "Gemuk, Kelebihan berat badan tingkat berat";
    }

    document.getElementById('hasil').innerHTML = "Hasil perhitungan BMI : " + hasil.toFixed(1);
    document.getElementById('keterangan').innerHTML = "Keterangan : " + keterangan;
    document.getElementById('air').innerHTML = "Hasil perhitungan Kebutuhan air : " + air.toFixed(0) + " ml";

}

// slider
berat.addEventListener("change", sliderbrt);
berat1.addEventListener("change", sliderbrt);
tinggi.addEventListener("change", slidertng);
tinggi1.addEventListener("change", slidertng);

function sliderbrt(event){
    if (parseInt(event.target.value) <= parseInt(tinggi.value)){
        berat.value = tinggi.value;
        berat1.value = tinggi1.value;
    }
}
function slidertng(event){
    if (parseInt(event.target.value) <= parseInt(berat.value)){
        tinggi.value = berat.value;
        tinggi1.value = berat1.value;
    }
}