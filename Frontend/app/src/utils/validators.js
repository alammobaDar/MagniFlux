export function isValid(B, A, theta, angleUnit){
    if (isNaN(B) || isNaN(A) || isNaN(theta) || B < 0 || A < 0){
        alert("Please enter a valid natural numeric value.")
        return false;
    }
    else if (angleUnit === "Degrees" && (theta < 0 || theta > 360)){
        alert("Angle(Degrees) is only between 0  to 360")
        return false;
    }
    else if (angleUnit === "Radians" && (theta < 0 || theta > 6.28)){
        alert("Angle(Radians) is only between 0 to 6.23")
        return false;
    }
    else{
        return true
    }
}