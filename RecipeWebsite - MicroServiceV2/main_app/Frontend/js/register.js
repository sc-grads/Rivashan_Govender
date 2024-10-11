document.getElementById("register-form").addEventListener("submit", async function (event) {
    event.preventDefault();  // Prevents the default form submission behavior

    const data = {
        username: document.getElementById("username").value,
        password: document.getElementById("password").value
    };

    try {
        const response = await fetch("http://localhost:8000/users/register", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        });

        if (response.ok) {
            // Handle success
            alert("Registration successful!");
            window.location.href = "/login"; // Redirect to login page
        } else {
            // Handle errors
            const errorData = await response.json();
            alert("Error: " + errorData.detail);
        }
    } catch (error) {
        console.error("Error during registration:", error);
    }
});
