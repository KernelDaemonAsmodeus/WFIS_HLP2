let nickname = "";
let lastBalance = null;
let spinning = false;

function startGame() {
    nickname = document.getElementById("nickname").value.trim();
    if (!nickname) {
        alert("Podaj nick.");
        return;
    }

    document.getElementById("start").style.display = "none";
    const welcome = document.getElementById("welcome");
    welcome.innerText = `Witaj, ${nickname}!`;
    welcome.style.display = "block";

    fetch("/start", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({nickname})
    }).then(r => r.json()).then(data => {
        document.getElementById("game").style.display = "block";
        document.getElementById("balance").innerText = data.balance;
        lastBalance = data.balance; // <- ustawiamy tu initial lastBalance
        document.getElementById("message").innerText = "";
    }).catch(err => {
        console.error(err);
        alert("Błąd startu gry.");
    });
}

function spin() {
    if (spinning) return;
    if (!nickname) { alert("Najpierw kliknij Start."); return; }
    if (lastBalance === null) { alert("Najpierw kliknij Start."); return; }

    const spinBtn = document.getElementById("spinBtn");
    spinBtn.disabled = true;
    spinning = true;

    fetch("/spin", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({nickname})
    }).then(r => r.json()).then(data => {
        if (data.error) {
            alert(data.error);
            spinBtn.disabled = false;
            spinning = false;
            return;
        }

        // różnica balansu
        const diff = data.balance - lastBalance;
        lastBalance = data.balance;

        const msg = document.getElementById("message");
        if (diff > 0) {
            msg.innerText = `🎉 Wygrałeś +${diff} punktów!`;
            msg.style.color = "green";
        } else if (diff < 0) {
            msg.innerText = `😢 Przegrałeś ${Math.abs(diff)} punktów.`;
            msg.style.color = "red";
        } else {
            msg.innerText = `Brak zmian w balansie.`;
            msg.style.color = "black";
        }

        document.getElementById("balance").innerText = data.balance;

        const items = document.getElementById("items");
        const roulette = document.getElementById("roulette");
        items.innerHTML = "";
        data.values.forEach((val, idx) => {
            const div = document.createElement("div");
            div.className = "item";
            div.innerText = val;
            if (idx === data.result_index) {
                div.dataset.result = "true";
            }
            items.appendChild(div);
        });

        // reset transform
        items.style.transition = "none";
        items.style.transform = "translateX(0px)";
        void items.offsetWidth;

        // znajdź element wyniku po indexie
        const resultEl = items.querySelector('[data-result="true"]');
        const containerWidth = roulette.clientWidth;
        const containerCenter = containerWidth / 2;
        const resultCenter = resultEl.offsetLeft + resultEl.offsetWidth / 2;
        const distance = containerCenter - resultCenter;

        // animacja
        items.style.transition = "transform 5s cubic-bezier(0.25, 1, 0.5, 1)";
        const onEnd = () => {
            resultEl.classList.add("highlight");
            spinBtn.disabled = false;
            spinning = false;
            items.removeEventListener("transitionend", onEnd);
        };
        items.addEventListener("transitionend", onEnd);

        items.style.transform = `translateX(${distance}px)`;
    });
}

function endGame() {
    if (!nickname) { alert("Nie rozpoczęto gry."); return; }
    fetch("/end", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({nickname})
    }).then(r => r.json()).then(data => {
        alert(data.message || "Zapisano wynik.");
        document.getElementById("game").style.display = "none";
        lastBalance = null;
        nickname = "";
        loadRanking();
    }).catch(err => {
        console.error(err);
        alert("Błąd zapisu wyniku.");
    });
}

function loadRanking() {
    fetch("/ranking")
        .then(r => r.json())
        .then(data => {
            const tbody = document.querySelector("#ranking tbody");
            tbody.innerHTML = "";
            data.forEach(row => {
                const tr = document.createElement("tr");
                tr.innerHTML = `
                    <td>${row.nickname}</td>
                    <td>${row.max_balance}</td>
                    <td>${row.spins}</td>
                `;
                tbody.appendChild(tr);
            });
        });
}

window.addEventListener("DOMContentLoaded", () => {
    loadRanking();
});
