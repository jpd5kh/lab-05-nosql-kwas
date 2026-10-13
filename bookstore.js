// Step 2: 
// use bookstore 
db = db.getSiblingDB("bookstore")

// Step 3: load authors.json
db.authors.drop()
doc = JSON.parse(fs.readFileSync("authors.json", "utf8"))
db.authors.insertMany(doc)

// Step 4: load books.json
db.books.drop()
doc = JSON.parse(fs.readFileSync("books.json", "utf8"))
db.books.insertMany(doc)

// Step 5: list authors and books
db.authors.find()
db.books.find()

// Step 6: insert two new books
db.books.insertOne({title: "Watership Down", published_year: 1972, author_ids: [ "author_004" ] })
db.books.insertOne({title: "The Last Train to London", published_year: 2019, author_ids: [ "author_005" ] })

// Step 7: add missing authors
db.authors.insertOne({ _id: "author_004", name: "Richard Adams", nationality: "British", bio: {short: "English novelist who wrote several fantasy books.", long: "Richard George Adams was an English novelist. He is best known for his debut novel Watership Down which achieved international acclaim. His other works included Maia, Shardik and The Plague Dogs. He studied Modern History at Worcester College, Oxford, before serving in the British Army during World War II."} })
db.authors.insertOne({_id: "author_005", name: "Meg Waite Clayton", nationality: "American", bio: {short: "American novelist and essayist who writes literary fiction books", long: "Meg Waite Clayton is an American novelist. A graduate of the University of Michigan Law School, Clayton also earned bachelor's degrees in History and Psychology from the University of Michigan. She worked as a lawyer at the Los Angeles firm of Latham & Watkins. She grew up primarily in suburban Kansas City and suburban Chicago, where she graduated from Glenbrook North High School.[2] She began writing in earnest after moving to a horse farm outside of Baltimore, Maryland, where her first novel is set. She now lives in the San Francisco Bay Area."} })

// Step 8: filter books by a list of authors
db.books.find({ author_ids: { $in: ["author_001", "author_005"] } })
