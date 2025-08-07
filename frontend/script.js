async function runQuery() {
  const queryInput = document.getElementById("query-input").value;

  const response = await fetch("http://127.0.0.1:5000/query", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ query: queryInput }),
  });

  const data = await response.json();

  const resultDiv = document.getElementById("result");
  if (data.error) {
    resultDiv.innerHTML = `<p style="color:red;">❌ ${data.error}</p>`;
  } else if (data.results.length === 0) {
    resultDiv.innerHTML = `<p>🟡 No results found.</p>`;
  } else {
    const table = document.createElement("table");
    const headers = Object.keys(data.results[0]);

    const thead = table.createTHead();
    const headRow = thead.insertRow();
    headers.forEach((header) => {
      const th = document.createElement("th");
      th.innerText = header;
      headRow.appendChild(th);
    });

    const tbody = table.createTBody();
    data.results.forEach((row) => {
      const tr = tbody.insertRow();
      headers.forEach((header) => {
        const td = tr.insertCell();
        td.innerText = row[header];
      });
    });

    resultDiv.innerHTML = "";
    resultDiv.appendChild(table);
  }
}
