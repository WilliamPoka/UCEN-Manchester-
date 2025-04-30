// the books go here !!! hashtags for notes > /* and // stupid design smh
//  BOOK DATA 
const books = [
    //Over £20 for a book that isnt volumes is crazy prices, INFLATION >:(
    {
        id: 1,
        title: "One Piece",
        author: "Eiichiro Oda",
        genre: "manga",
        price: 13.95,
        description: "Pirate adventures with Luffy and his crew!"
    },
    {
        id: 2,
        title: "Golden Kamuy",
        author: "Satoru Noda",
        genre: "manga",
        price: 12.00,
        description: "Treasure hunt in historical Japan!" //THIS IS SO SO SO SO SO SO GOOOD a bit wierd but still GOOD
    },
    {
        id: 3,
        title: "Monsters Of Men",
        author: "Patrick Ness",
        genre: "sci-fi",
        price: 9.00,
        description: "Final book in the Chaos Walking trilogy" //This was a good read when i was in highschool
    },
    {
        id: 4,
        title: "IT",
        author: "Stephen King",
        genre: "horror",
        price: 18.00,
        description: "Scary clown terrorizes a town"
    },
    {
        id: 5,
        title: "If I Did It",
        author: "O.J. Simpson",
        genre: "true-crime",
        price: 18.00,
        description: "Controversial crime story"
    },
    {
        id: 6,
        title: "Fourth Wing",
        author: "Rebecca Yarros",
        genre: "fantasy",
        price: 18.75,
        description: "Dragon rider academy romance" //Sisters request
    },
    {
        id: 7,
        title: "My Hero Academia, Vol. 1",
        author: "Kohei Horikoshi",
        genre: "manga",
        price: 9.99,  
        description: "Izuku Midoriya meets All Might and begins his superhero journey!"
    },
    {
        id: 8,
        title: "Warhammer 40,000: Horus Rising",
        author: "Dan Abnett",
        genre: "sci-fi",
        price: 12.50,
        description: "The Horus Heresy begins in this grimdark space opera." //WARHAMMER GEEK
    },
    {
        id: 9,
        title: "The Silent Patient",
        author: "Alex Michaelides",
        genre: "mystery",
        price: 18.75,
        description: "A psychological thriller about a woman who shoots her husband."
    },
    {
        id: 10,
        title: "Warhammer: Gotrek & Felix Omnibus",
        author: "William King",
        genre: "fantasy",
        price: 22.99,
        description: "A dwarf slayer and human poet battle monsters in the Old World."
    },
    {
        id: 11,
        title: "My Hero Academia: School Briefs, Vol. 1",
        author: "Anri Yoshi",
        genre: "manga",
        price: 14.20,
        description: "Slice-of-life stories from UA High School."
    },
    {
        id: 12,
        title: "Warhammer 40,000: Xenos",
        author: "Dan Abnett",
        genre: "sci-fi",
        price: 27.50,
        description: "Inquisitor Eisenhorn hunts heretics in the 41st millennium."
    },
    {
        id: 13,
        title: "The Shining",
        author: "Stephen King",  
        genre: "horror",
        price: 18.50,
        description: "A haunted hotel drives a caretaker to madness." //Only watched the movies icl
    },
    {
        id: 14,
        title: "House of Leaves",
        author: "Mark Z. Danielewski",  
        genre: "horror",
        price: 22.99,
        description: "A mind-bending story about a house larger inside than outside."
    },
    {
        id: 15,
        title: "Chainsaw Man, Vol. 1",
        author: "Tatsuki Fujimoto",  
        genre: "manga",
        price: 11.25,
        description: "A devil hunter merges with his chainsaw demon partner."
    }

    
];
//the id was supposed to be for a favourites feature but i couldnt be bothered to be honest ToT

// this is to connect to html elements (very annoying because capitalisation matters 😴)
const form = document.getElementById('book-form');
const resultsSection = document.getElementById('results');
const bookResults = document.getElementById('book-results');

// this is for input and data when submitted
form.addEventListener('submit', function(e) {
    e.preventDefault(); 
    
    // Get user's search choices
    const genre = document.getElementById('genre').value;
    const author = document.getElementById('author').value.toLowerCase();
    const price = document.getElementById('price').value;
    
// this is jus filtering stuff
    const filteredBooks = books.filter(book => {
        //  checks the genre
        if (genre && genre !== "any" && book.genre !== genre) return false;
        
        // Checks the author name
        if (author && !book.author.toLowerCase().includes(author)) return false;
        
        // Check price range, moeny 🤑
        if (price === "0-10" && book.price > 10) return false;
        if (price === "10-20" && (book.price <= 10 || book.price > 20)) return false;
        if (price === "20+" && book.price <= 20) return false;
        
        return true; // Keep book if all checks pass
    });
    
    // Show the results
    displayResults(filteredBooks);
});

// result
function displayResults(filteredBooks) {
    // Clear previous results
    bookResults.innerHTML = '';
    
    // Show message if no books found
    if (filteredBooks.length === 0) {
        bookResults.innerHTML = '<p>No books found. Try different filters!</p>';
        return;
    }
    
    // Create HTML for each book
    filteredBooks.forEach(book => {
        const bookElement = document.createElement('div');
        bookElement.className = 'book-card';
        bookElement.innerHTML = `
            <h3>${book.title}</h3>
            <p><strong>Author:</strong> ${book.author}</p>
            <p><strong>Price:</strong> £${book.price.toFixed(2)}</p>
            <p><strong>Genre:</strong> ${book.genre}</p>
            <p>${book.description}</p>
        `;
        bookResults.appendChild(bookElement);
        //GET RID OF THE CHILDREN 👺
    });
    
    // Show the results section
    resultsSection.classList.remove('hidden');
    
console.log("Filters:", { genre, author, price });

console.log("Matched Books:", filteredBooks.map(b => b.title));
}