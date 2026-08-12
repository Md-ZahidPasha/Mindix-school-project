<script lang="ts">
    import PrincipalSidebar from '$lib/components/principal/PrincipalSidebar.svelte';
    type BookStatus = 'available' | 'unavailable';

    type Book = {
        id: string;
        name: string;
        author: string;
        category: string;
        status: BookStatus;
        availableDate: string;
    };

    type BookRecord = {
        id: number;
        bookName: string;
        issueDate: string;
        returnDate: string;
        status: 'Borrowed' | 'Returned';
    };

    let searchBook = $state('');

    let searchedBook = $state<Book | null>(null);

    let searchMessage = $state('');

    let requestMessage = $state('');

    const books: Book[] = [
        {
            id: 'BK001',
            name: 'The Great Gatsby',
            author: 'F. Scott Fitzgerald',
            category: 'Literature',
            status: 'available',
            availableDate: 'Available Now'
        },
        {
            id: 'BK002',
            name: 'Introduction to Biology',
            author: 'Campbell',
            category: 'Biology',
            status: 'available',
            availableDate: 'Available Now'
        },
        {
            id: 'BK003',
            name: 'Advanced Mathematics',
            author: 'R. D. Sharma',
            category: 'Mathematics',
            status: 'unavailable',
            availableDate: '25 Aug 2026'
        },
        {
            id: 'BK004',
            name: 'English Grammar',
            author: 'Wren & Martin',
            category: 'English',
            status: 'available',
            availableDate: 'Available Now'
        },
        {
            id: 'BK005',
            name: 'Computer Fundamentals',
            author: 'P. K. Sinha',
            category: 'Computer Science',
            status: 'unavailable',
            availableDate: '29 Aug 2026'
        }
    ];

    let bookRecords = $state<BookRecord[]>([
        {
            id: 1,
            bookName: 'School Management Handbook',
            issueDate: '02 Aug 2026',
            returnDate: '09 Aug 2026',
            status: 'Returned'
        },
        {
            id: 2,
            bookName: 'Educational Leadership',
            issueDate: '28 Jul 2026',
            returnDate: '28 Aug 2026',
            status: 'Borrowed'
        },
        {
            id: 3,
            bookName: 'The Great Gatsby',
            issueDate: '15 Jul 2026',
            returnDate: '22 Jul 2026',
            status: 'Returned'
        }
    ]);

    function searchForBook() {
        requestMessage = '';

        const query = searchBook.trim().toLowerCase();

        if (!query) {
            searchedBook = null;
            searchMessage = 'Please enter a book name.';
            return;
        }

        const result = books.find((book) =>
            book.name.toLowerCase().includes(query)
        );

        if (result) {
            searchedBook = result;
            searchMessage = '';
        } else {
            searchedBook = null;
            searchMessage = 'No book found with this name.';
        }
    }

    function requestBook() {
        if (!searchedBook) return;

        if (searchedBook.status === 'available') {
            requestMessage =
                'Book request submitted successfully. Waiting for library approval.';
        } else {
            requestMessage =
                `This book is currently unavailable. Expected availability: ${searchedBook.availableDate}.`;
        }
    }

    function clearSearch() {
        searchBook = '';
        searchedBook = null;
        searchMessage = '';
        requestMessage = '';
    }
</script>

<div class="principal-layout">

    <PrincipalSidebar />

    <main class="main-content">

<div class="library-page">

    <!-- PAGE HEADER -->

    <header class="page-header">
        <div>
            <h1>Library</h1>

            <p>
                Search books, check availability and view your library records.
            </p>
        </div>
    </header>


    <!-- SEARCH BOOK -->

    <section class="search-card">

        <div class="section-heading">
            <div class="heading-icon">
                ▥
            </div>

            <div>
                <h2>Find a Book</h2>

                <p>
                    Enter the name of the book you want to find in the library.
                </p>
            </div>
        </div>


        <div class="search-row">

            <div class="search-input-wrapper">

                <label for="book-search">
                    Book Name
                </label>

                <input
                    id="book-search"
                    type="text"
                    bind:value={searchBook}
                    placeholder="Enter book name..."
                    onkeydown={(event) => {
                        if (event.key === 'Enter') {
                            searchForBook();
                        }
                    }}
                />

            </div>


            <button
                type="button"
                class="search-button"
                onclick={searchForBook}
            >
                Search
            </button>

        </div>


        {#if searchMessage}

            <div class="message error-message">
                {searchMessage}
            </div>

        {/if}

    </section>


    <!-- SEARCH RESULT -->

    {#if searchedBook}

        <section class="book-result-card">

            <div class="result-header">

                <div>
                    <span class="result-label">
                        BOOK DETAILS
                    </span>

                    <h2>
                        {searchedBook.name}
                    </h2>

                    <p>
                        {searchedBook.author}
                    </p>
                </div>


                <button
                    type="button"
                    class="close-button"
                    onclick={clearSearch}
                    aria-label="Clear search"
                >
                    ×
                </button>

            </div>


            <div class="book-details">

                <div class="book-detail">
                    <span>Book ID</span>
                    <strong>{searchedBook.id}</strong>
                </div>


                <div class="book-detail">
                    <span>Category</span>
                    <strong>{searchedBook.category}</strong>
                </div>


                <div class="book-detail">
                    <span>Author</span>
                    <strong>{searchedBook.author}</strong>
                </div>


                <div class="book-detail">
                    <span>Availability</span>

                    {#if searchedBook.status === 'available'}

                        <strong class="available">
                            Available
                        </strong>

                    {:else}

                        <strong class="unavailable">
                            Not Available
                        </strong>

                    {/if}
                </div>

            </div>


            <!-- AVAILABILITY -->

            {#if searchedBook.status === 'available'}

                <div class="availability-box available-box">

                    <div class="availability-icon">
                        ✓
                    </div>

                    <div>
                        <strong>
                            Book is available
                        </strong>

                        <p>
                            You can request this book from the library.
                        </p>
                    </div>

                </div>


                <button
                    type="button"
                    class="request-button"
                    onclick={requestBook}
                >
                    Request / Book This Book
                </button>

            {:else}

                <div class="availability-box unavailable-box">

                    <div class="availability-icon">
                        !
                    </div>

                    <div>
                        <strong>
                            Book is currently unavailable
                        </strong>

                        <p>
                            Expected availability:
                            <b>{searchedBook.availableDate}</b>
                        </p>
                    </div>

                </div>

            {/if}


            {#if requestMessage}

                <div class="message success-message">
                    {requestMessage}
                </div>

            {/if}

        </section>

    {/if}


    <!-- MY LIBRARY RECORDS -->

    <section class="records-section">

        <div class="section-title">

            <div>
                <h2>My Library Records</h2>

                <p>
                    View books borrowed and returned by you.
                </p>
            </div>

            <span class="record-count">
                {bookRecords.length} Records
            </span>

        </div>


        <div class="records-card">

            <div class="table-wrapper">

                <table>

                    <thead>

                        <tr>
                            <th>Book Name</th>
                            <th>Issue Date</th>
                            <th>Return Date</th>
                            <th>Status</th>
                        </tr>

                    </thead>


                    <tbody>

                        {#each bookRecords as record}

                            <tr>

                                <td>
                                    <div class="book-name">
                                        <div class="small-book-icon">
                                            ▥
                                        </div>

                                        <strong>
                                            {record.bookName}
                                        </strong>
                                    </div>
                                </td>


                                <td>
                                    {record.issueDate}
                                </td>


                                <td>
                                    {record.returnDate}
                                </td>


                                <td>

                                    {#if record.status === 'Borrowed'}

                                        <span class="status borrowed">
                                            Borrowed
                                        </span>

                                    {:else}

                                        <span class="status returned">
                                            Returned
                                        </span>

                                    {/if}

                                </td>

                            </tr>

                        {/each}

                    </tbody>

                </table>

            </div>

        </div>

    </section>
</div>
    </main>
</div>


<style>
    .principal-layout {
        display: flex;
        min-height: 100vh;
        background: #f7f9fc;
    }

    .main-content {
        flex: 1;
        min-width: 0;
    }

    .library-page {
        min-height: 100vh;
        padding: 28px 32px;
        box-sizing: border-box;
        background: #f7f9fc;
    }


    /* HEADER */

    .page-header {
        margin-bottom: 24px;
    }

    .page-header h1 {
        margin: 0;
        color: #14213d;
        font-size: 30px;
    }

    .page-header p {
        margin: 7px 0 0;
        color: #64748b;
        font-size: 15px;
    }


    /* SEARCH CARD */

    .search-card {
        padding: 24px;
        background: white;
        border: 1px solid #e5eaf2;
        border-radius: 16px;
        box-shadow:
            0 4px 14px
            rgba(15, 23, 42, 0.03);
    }


    .section-heading {
        display: flex;
        align-items: center;
        gap: 13px;
        margin-bottom: 20px;
    }


    .heading-icon {
        width: 44px;
        height: 44px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 12px;
        background: #eef4ff;
        color: #2563eb;
        font-size: 20px;
    }


    .section-heading h2 {
        margin: 0;
        color: #14213d;
        font-size: 19px;
    }


    .section-heading p {
        margin: 4px 0 0;
        color: #64748b;
        font-size: 12px;
    }


    .search-row {
        display: flex;
        align-items: flex-end;
        gap: 12px;
    }


    .search-input-wrapper {
        flex: 1;
    }


    .search-input-wrapper label {
        display: block;
        margin-bottom: 7px;
        color: #334155;
        font-size: 12px;
        font-weight: 600;
    }


    .search-input-wrapper input {
        width: 100%;
        height: 44px;
        padding: 0 13px;
        box-sizing: border-box;
        border: 1px solid #dbe3ef;
        border-radius: 9px;
        background: white;
        color: #1e293b;
        font-size: 13px;
        outline: none;
    }


    .search-input-wrapper input:focus {
        border-color: #2563eb;
        box-shadow:
            0 0 0 3px
            rgba(37, 99, 235, 0.1);
    }


    .search-button {
        height: 44px;
        padding: 0 25px;
        border: none;
        border-radius: 9px;
        background: #2563eb;
        color: white;
        font-size: 13px;
        font-weight: 600;
        cursor: pointer;
    }


    .search-button:hover {
        background: #1d4ed8;
    }


    /* BOOK RESULT */

    .book-result-card {
        margin-top: 20px;
        padding: 24px;
        background: white;
        border: 1px solid #e5eaf2;
        border-radius: 16px;
        box-shadow:
            0 4px 14px
            rgba(15, 23, 42, 0.03);
    }


    .result-header {
        display: flex;
        align-items: flex-start;
        justify-content: space-between;
        padding-bottom: 18px;
        border-bottom: 1px solid #edf1f6;
    }


    .result-label {
        display: block;
        margin-bottom: 6px;
        color: #2563eb;
        font-size: 10px;
        font-weight: 700;
        letter-spacing: 0.7px;
    }


    .result-header h2 {
        margin: 0;
        color: #14213d;
        font-size: 21px;
    }


    .result-header p {
        margin: 5px 0 0;
        color: #64748b;
        font-size: 12px;
    }


    .close-button {
        width: 32px;
        height: 32px;
        border: none;
        border-radius: 8px;
        background: #f1f5f9;
        color: #64748b;
        font-size: 21px;
        cursor: pointer;
    }


    .close-button:hover {
        background: #e2e8f0;
    }


    .book-details {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 14px;
        padding: 20px 0;
    }


    .book-detail {
        padding: 13px;
        border: 1px solid #e5eaf2;
        border-radius: 10px;
        background: #f8fafc;
    }


    .book-detail span {
        display: block;
        margin-bottom: 6px;
        color: #94a3b8;
        font-size: 10px;
        font-weight: 600;
    }


    .book-detail strong {
        color: #334155;
        font-size: 12px;
    }


    .available {
        color: #16a34a !important;
    }


    .unavailable {
        color: #dc2626 !important;
    }


    /* AVAILABILITY */

    .availability-box {
        display: flex;
        align-items: center;
        gap: 13px;
        padding: 14px;
        border-radius: 10px;
    }


    .available-box {
        background: #f0fdf4;
        border: 1px solid #bbf7d0;
    }


    .unavailable-box {
        background: #fff7ed;
        border: 1px solid #fed7aa;
    }


    .availability-icon {
        width: 36px;
        height: 36px;
        flex-shrink: 0;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 50%;
        font-weight: 800;
    }


    .available-box .availability-icon {
        background: #dcfce7;
        color: #16a34a;
    }


    .unavailable-box .availability-icon {
        background: #ffedd5;
        color: #ea580c;
    }


    .availability-box strong {
        display: block;
        color: #334155;
        font-size: 12px;
    }


    .availability-box p {
        margin: 4px 0 0;
        color: #64748b;
        font-size: 11px;
    }


    .request-button {
        width: 100%;
        height: 42px;
        margin-top: 12px;
        border: none;
        border-radius: 9px;
        background: #2563eb;
        color: white;
        font-size: 13px;
        font-weight: 600;
        cursor: pointer;
    }


    .request-button:hover {
        background: #1d4ed8;
    }


    /* RECORDS */

    .records-section {
        margin-top: 28px;
    }


    .section-title {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 15px;
        margin-bottom: 14px;
    }


    .section-title h2 {
        margin: 0;
        color: #14213d;
        font-size: 20px;
    }


    .section-title p {
        margin: 5px 0 0;
        color: #64748b;
        font-size: 13px;
    }


    .record-count {
        padding: 7px 11px;
        border-radius: 8px;
        background: #eef4ff;
        color: #2563eb;
        font-size: 11px;
        font-weight: 700;
    }


    .records-card {
        overflow: hidden;
        background: white;
        border: 1px solid #e5eaf2;
        border-radius: 16px;
        box-shadow:
            0 4px 14px
            rgba(15, 23, 42, 0.03);
    }


    .table-wrapper {
        overflow-x: auto;
    }


    table {
        width: 100%;
        border-collapse: collapse;
        min-width: 650px;
    }


    th {
        padding: 15px 20px;
        background: #f8fafc;
        color: #64748b;
        font-size: 11px;
        font-weight: 700;
        text-align: left;
        border-bottom: 1px solid #e5eaf2;
    }


    td {
        padding: 16px 20px;
        color: #64748b;
        font-size: 12px;
        border-bottom: 1px solid #edf1f6;
    }


    tr:last-child td {
        border-bottom: none;
    }


    .book-name {
        display: flex;
        align-items: center;
        gap: 10px;
    }


    .small-book-icon {
        width: 32px;
        height: 32px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 8px;
        background: #eef4ff;
        color: #2563eb;
    }


    .book-name strong {
        color: #14213d;
        font-size: 12px;
    }


    .status {
        display: inline-block;
        padding: 6px 9px;
        border-radius: 7px;
        font-size: 10px;
        font-weight: 700;
    }


    .borrowed {
        background: #fff7ed;
        color: #ea580c;
    }


    .returned {
        background: #f0fdf4;
        color: #16a34a;
    }


    /* MESSAGES */

    .message {
        margin-top: 14px;
        padding: 11px 13px;
        border-radius: 9px;
        font-size: 11px;
    }


    .error-message {
        background: #fef2f2;
        border: 1px solid #fecaca;
        color: #dc2626;
    }


    .success-message {
        background: #f0fdf4;
        border: 1px solid #bbf7d0;
        color: #15803d;
    }


    /* RESPONSIVE */

    @media (max-width: 900px) {

        .library-page {
            padding: 22px;
        }


        .book-details {
            grid-template-columns: repeat(2, 1fr);
        }

    }


    @media (max-width: 600px) {

        .library-page {
            padding: 18px;
        }


        .search-row {
            flex-direction: column;
            align-items: stretch;
        }


        .search-button {
            width: 100%;
        }


        .book-details {
            grid-template-columns: 1fr;
        }


        .section-title {
            align-items: flex-start;
            flex-direction: column;
        }

    }

</style>