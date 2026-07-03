async function loadUsers(){

    const response = await fetch("/api/users");

    const data = await response.json();

    document.getElementById("output").textContent =
        JSON.stringify(data,null,4);

}

async function loadProducts(){

    const response = await fetch("/api/products");

    const data = await response.json();

    document.getElementById("output").textContent =
        JSON.stringify(data,null,4);

}