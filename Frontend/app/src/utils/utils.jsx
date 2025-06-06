export async function SendInputsForExplanation(newPost) {
    const response = await fetch("http://127.0.0.1:8000/api/explain/", {
                method: 'POST',
                headers:{'Content-type': 'application/json'},
                body: JSON.stringify(newPost),
            })  
            if (!response.ok){
                throw new Error("Failed to POST")
            }
            return await response.json();
}

export async function SendText(newPost) {
    const response = await fetch("http://127.0.0.1:8000/api/ai/", {
        method: 'POST',
        headers:{'Content-type': 'application/json'},
        body: JSON.stringify(newPost),
    })  
    if (!response.ok){
        throw new Error("Failed to POST")
    }
    return await response.json();
}