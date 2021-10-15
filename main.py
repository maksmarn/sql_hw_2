from smartninja_sql.sqlite import SQLiteDatabase

db = SQLiteDatabase("Chinook_Sqlite.sqlite")

db.print_tables(verbose=True)


def most_expensive():
    db.pretty_print("""SELECT *
                    FROM Invoice
                    WHERE Total = (SELECT MAX(Total) FROM Invoice);""")


most_expensive()


def the_cheapest():
    db.pretty_print("""SELECT *
                    FROM Invoice
                    WHERE Total = (SELECT MIN(Total) FROM Invoice);""")


the_cheapest()


def most_popular_city():
    db.pretty_print("""SELECT Invoice.BillingCity, COUNT(*) AS the_count
                    FROM Invoice
                    GROUP BY Invoice.BillingCity
                    ORDER BY the_count DESC;""")


most_popular_city()


def protected_aac():
    db.pretty_print("""SELECT COUNT(TrackId) AS AacCount
                    FROM Track
                    WHERE MediaTypeId = 3;""")


protected_aac()


def biggest_artist():
    db.pretty_print("""SELECT Artist.Name, COUNT(*) Album_count
                    FROM Artist
                    JOIN Album ON Album.ArtistId = Artist.ArtistId
                    GROUP BY Album.ArtistId
                    ORDER BY Album_count DESC;""")


biggest_artist()


def biggest_genre():
    db.pretty_print("""SELECT Genre.Name, COUNT(*) Track_count
                    FROM Genre
                    JOIN Track ON Track.GenreId = Genre.GenreId
                    GROUP BY Track.GenreId
                    ORDER BY Track_count DESC""")


biggest_genre()


def biggest_customer():
    db.pretty_print("""SELECT Customer.FirstName, Customer.LastName, SUM(Invoice.Total) AS Money_count
    FROM Customer
    JOIN Invoice on Invoice.CustomerId = Customer.CustomerId
    GROUP BY Invoice.CustomerId
    ORDER BY Money_count DESC""")


biggest_customer()


def tracks_by_invoice():
    db.pretty_print("""SELECT Invoice.InvoiceId, Track.Name
    FROM Invoice
    JOIN InvoiceLine ON Invoice.InvoiceId = InvoiceLine.InvoiceId
    JOIN Track ON InvoiceLine.TrackId = Track.TrackId""")


tracks_by_invoice()
