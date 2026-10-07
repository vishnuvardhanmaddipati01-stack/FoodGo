/* =========================================
   FOODGO - MAIN JAVASCRIPT
   ========================================= */


const API_BASE_URL = "http://127.0.0.1:8000/api";


/* =========================================
   LOAD CATEGORIES
   ========================================= */

async function loadCategories() {

    const container =
        document.getElementById("categoryContainer");

    if (!container) {
        return;
    }

    try {

        const response =
            await fetch(
                API_BASE_URL + "/categories/"
            );

        if (!response.ok) {
            throw new Error("Unable to load categories");
        }

        const categories =
            await response.json();

        container.innerHTML = "";

        if (categories.length === 0) {

            container.innerHTML =
                "<p>No categories available.</p>";

            return;
        }

        categories.forEach(function(category) {

            const card =
                document.createElement("div");

            card.className = "category-card";

            card.innerHTML = `

                <img
                    src="${
                        category.image ||
                        "https://via.placeholder.com/150?text=Food"
                    }"
                    alt="${category.name}"
                >

                <h3>
                    ${category.name}
                </h3>

            `;

            container.appendChild(card);

        });

    }

    catch (error) {

        console.error(
            "Category error:",
            error
        );

        container.innerHTML = `

            <p>
                Unable to load categories.
            </p>

        `;

    }

}


/* =========================================
   LOAD RESTAURANTS
   ========================================= */

async function loadRestaurants() {

    const container =
        document.getElementById(
            "restaurantContainer"
        );

    if (!container) {
        return;
    }

    try {

        const response =
            await fetch(
                API_BASE_URL + "/restaurants/"
            );

        if (!response.ok) {
            throw new Error(
                "Unable to load restaurants"
            );
        }

        const restaurants =
            await response.json();

        container.innerHTML = "";

        if (restaurants.length === 0) {

            container.innerHTML =
                "<p>No restaurants available.</p>";

            return;
        }

        restaurants
            .slice(0, 6)
            .forEach(function(restaurant) {

                const card =
                    document.createElement(
                        "div"
                    );

                card.className =
                    "restaurant-card";

                card.innerHTML = `

                    <img
                        src="${
                            restaurant.image ||
                            "https://via.placeholder.com/300x180?text=Restaurant"
                        }"
                        alt="${restaurant.name}"
                    >

                    <h3>
                        ${restaurant.name}
                    </h3>

                    <p>
                        ⭐ ${restaurant.rating}
                    </p>

                    <p>
                        ${restaurant.address}
                    </p>

                    <button
                        class="view-menu-button"
                    >
                        View Menu
                    </button>

                `;

                const button =
                    card.querySelector(
                        ".view-menu-button"
                    );

                button.addEventListener(
                    "click",
                    function() {

                        localStorage.setItem(
                            "selectedRestaurantId",
                            restaurant.id
                        );

                        localStorage.setItem(
                            "selectedRestaurantName",
                            restaurant.name
                        );

                        window.location.href =
                            "/restaurant/";

                    }
                );

                container.appendChild(card);

            });

    }

    catch (error) {

        console.error(
            "Restaurant error:",
            error
        );

        container.innerHTML = `

            <p>
                Unable to load restaurants.
            </p>

        `;

    }

}


/* =========================================
   PAGE START
   ========================================= */

document.addEventListener(
    "DOMContentLoaded",
    function() {

        loadCategories();

        loadRestaurants();

    }
);