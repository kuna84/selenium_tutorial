// Array to store book data
var books = [
{
    title: "1984",
    author: "George Orwell",
    publicationYear: "1949",
    genre: "Dystopian",
    pages: "328",
    cover: "Paperback",
},
{
    title: "Foundation",
    author: "Isaac Asimov",
    publicationYear: "1951",
    genre: "Science Fiction",
    pages: "255",
    cover: "Paperback",
},
{
    title: "Dune",
    author: "Frank Herbert",
    publicationYear: "1965",
    genre: "Science Fiction",
    pages: "412",
    cover: "Paperback",
},
{
    title: "The Man in the High Castle",
    author: "Philip K. Dick",
    publicationYear: "1962",
    genre: "Science Fiction",
    pages: "273",
    cover: "Paperback",
},
{
    title: "Solaris",
    author: "Stanisław Lem",
    publicationYear: "1961",
    genre: "Science Fiction",
    pages: "204",
    cover: "Paperback",
},
];

// Function to show the modal
function showModal() {
document.getElementById("addBookModal").style.display = "block";
}

// Function to close the modal
function closeModal() {
document.getElementById("addBookModal").style.display = "none";
}

// Function to add a new book
function addBook(event) {
event.preventDefault();

// Get form input values
var title = document.getElementById("title").value;
var author = document.getElementById("author").value;
var publicationYear = document.getElementById("publicationYear").value;
var genre = document.getElementById("genre").value;
var pages = document.getElementById("pages").value;
var cover = document.getElementById("cover").value;

// Create a new book object
var book = {
    title: title,
    author: author,
    publicationYear: publicationYear,
    genre: genre,
    pages: pages,
    cover: cover,
};

// Add the book to the array
books.push(book);

// Reset form inputs
document.getElementById("bookForm").reset();

// Refresh the book table
refreshTable();

// Close the modal
closeModal();
}

// Function to refresh the book table
function refreshTable() {
var table = document.getElementById("booksDatabase");

// Clear the table body
table.innerHTML = `
    <tr>
        <th onclick="sortTable(0)" id="titleHeader">Title</th>
        <th onclick="sortTable(1)" id="authorHeader">Author</th>
        <th onclick="sortTable(2)" id="publicationYearHeader">Year of publication</th>
        <th onclick="sortTable(3)" id="genreHeader">Genre</th>
        <th onclick="sortTable(4)" id="pagesHeader">Number of pages</th>
        <th onclick="sortTable(5)" id="coverHeader">Cover Type</th>
        <th>Actions</th>
    </tr>
`;

// Populate the table with book data
for (var i = 0; i < books.length; i++) {
    var book = books[i];

    var row = document.createElement("tr");
    row.innerHTML = `
        <td>${book.title}</td>
        <td>${book.author}</td>
        <td>${book.publicationYear}</td>
        <td>${book.genre}</td>
        <td>${book.pages}</td>
        <td>${book.cover}</td>
        <td>
            <button onclick="editBook(${i})">Edit</button>
            <button onclick="deleteBook(${i})">Delete</button>
        </td>
    `;

    table.appendChild(row);
}
}

// Function to edit a book
function editBook(index) {
var book = books[index];

// Fill the form with book data
document.getElementById("title").value = book.title;
document.getElementById("author").value = book.author;
document.getElementById("publicationYear").value = book.publicationYear;
document.getElementById("genre").value = book.genre;
document.getElementById("pages").value = book.pages;
document.getElementById("cover").value = book.cover;

// Remove the book from the array
books.splice(index, 1);

// Refresh the book table
refreshTable();

// Show the modal
showModal();
}

// Function to delete a book
function deleteBook(index) {
// Remove the book from the array
books.splice(index, 1);

// Refresh the book table
refreshTable();
}

// Function to sort the table by column
function sortTable(columnIndex) {
var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
table = document.getElementById("booksDatabase");
switching = true;
// Set the sorting direction to ascending:
dir = "asc";
/* Make a loop that will continue until
no switching has been done: */
while (switching) {
    // Start by saying: no switching is done:
    switching = false;
    rows = table.rows;
    /* Loop through all table rows (except the
    first, which contains table headers): */
    for (i = 1; i < (rows.length - 1); i++) {
        // Start by saying there should be no switching:
        shouldSwitch = false;
        /* Get the two elements you want to compare,
        one from current row and one from the next: */
        x = rows[i].getElementsByTagName("TD")[columnIndex];
        y = rows[i + 1].getElementsByTagName("TD")[columnIndex];
        /* Check if the two rows should switch place,
        based on the direction, asc or desc: */
        if (dir == "asc") {
            if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
                // If so, mark as a switch and break the loop:
                shouldSwitch = true;
                break;
            }
        } else if (dir == "desc") {
            if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
                // If so, mark as a switch and break the loop:
                shouldSwitch = true;
                break;
            }
        }
    }
    if (shouldSwitch) {
        /* If a switch has been marked, make the switch
        and mark that a switch has been done: */
        rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
        switching = true;
        // Each time a switch is done, increase switchcount by 1:
        switchcount++;
    } else {
        /* If no switching has been done AND the direction is "asc",
        set the direction to "desc" and run the while loop again. */
        if (switchcount == 0 && dir == "asc") {
            dir = "desc";
            switching = true;
        }
    }
}
}
