// LAB: 4.1.12
// CMD (install package readline-sync): npm install readline-sync
// CMD (run program): node lab5_1.js
const readlineSync = require('readline-sync');

let contacts = [{
    name: "Maxwell Wright",
    phone: "(0191) 719 6495",
    email: "Curabitur.egestas.nunc@nonummyac.co.uk"
}, {
    name: "Raja Villarreal",
    phone: "0866 398 2895",
    email: "posuere.vulputate@sed.com"
}, {
    name: "Helen Richards",
    phone: "0800 1111",
    email: "libero@convallis.edu"
}];

// function showContact(choice) {
//     if (choice === "first") {
//         if (contacts.length > 0) {
//             console.log("First Contact:");
//             console.log("  Name:", contacts[0].name);
//             console.log("  Phone:", contacts[0].phone);
//             console.log("  Email:", contacts[0].email);
//         } else {
//             console.log("There are no contacts in the list.");
//         }
//     } else if (choice === "last") {
//         if (contacts.length > 0) {
//             const lastIndex = contacts.length - 1;
//             console.log("Last Contact:");
//             console.log("  Name:", contacts[lastIndex].name);
//             console.log("  Phone:", contacts[lastIndex].phone);
//             console.log("  Email:", contacts[lastIndex].email);
//         } else {
//             console.log("There are no contacts in the list.");
//         }
//     } else if (choice === "all") {
//         if (contacts.length > 0) {
//             console.log("All Contacts:");
//             for (let i = 0; i < contacts.length; i++) {
//                 console.log(`  Contact ${i + 1}:`); // Backticks allow "template literals" for easy variable interpolation.
//                 console.log("    Name:", contacts[i].name);
//                 console.log("    Phone:", contacts[i].phone);
//                 console.log("    Email:", contacts[i].email);
//             }
//         } else {
//             console.log("There are no contacts in the list.");
//         }
//     } else {
//         console.log("Invalid choice. Please enter 'first', 'last', 'all', or 'new'");
//     }
// }


function showContact(contactList, index) {
    // 1. Check if contactList is an array
    if (!(contactList instanceof Array)) {
        console.log("Error: The first argument must be an array of contacts.");
        return false; // Indicate failure
    }

    // 2. Check if the index is valid
    if (index < 0 || index >= contactList.length || typeof index !== 'number') {
        console.log("Error: Invalid contact index or no contact at this position.");
        return false;
    }

    // 3. Display the contact
    const contact = contactList[index];
    console.log("  Name:", contact.name);
    console.log("    Phone:", contact.phone);
    console.log("    Email:", contact.email);
    return true; // Indicate success
}

function showAllContacts(contactList) {
    if (!(contactList instanceof Array)) {
        console.log("Error: The argument must be an array of contacts.");
        return false;
    }

    if (contactList.length === 0) {
        console.log("There are no contacts in the list.");
        return true; // Still success, just no contacts
    }

    console.log("Contacts:");
    for (let i = 0; i < contactList.length; i++) {
        console.log(`Contact ${i + 1}:`);
        showContact(contactList, i); // Re-use showContact to display each individual contact for better modularity
    }
    return true;
}


function addContact() {
    let name = readlineSync.question("Enter contact name: ");
    let phone = readlineSync.question("Enter contact phone number: ");
    let email = readlineSync.question("Enter contact email: ");

    // Validate data
    if (name && phone && email) {
        contacts.push({name, phone, email});
        console.log("Contact added successfully!");
    } else {
        console.log("Please enter all required information (name, phone, email).");
    }
}

function addNewContact(contactList, name, phone, email) {
    if (!(contactList instanceof Array)) {
        console.log("Error: The first argument must be an array of contacts.");
        return false;
    }

    // Check if new contact data have any value
    if (!name || !phone || !email) {
        console.log("Error: Please provide name, phone, and email for the new contact.");
        return false;
    }

    contactList.push({ name, phone, email });
    console.log("Contact added successfully!");
    return true;
}


function manageContacts() {
    choice = readlineSync.question("What do you want to do? (first/last/all/new/quit): ");

    // switch (choice.toLowerCase()) {
    //     case "first":
    //     case "last":
    //     case "all":
    //         showContact(choice);
    //         break;
    //     case "new":
    //         addContact();
    //         break;
    //     case "quit":
    //         console.log("Exiting program.");
    //         break;
    //     default:
    //         console.log("Invalid choice. Please enter 'first', 'last', 'all', 'new', or 'quit'");
    // }

    // ... inside the manageContacts function ...
    switch (choice.toLowerCase()) {
        case "first":
            if (contacts.length > 0) {
                console.log("First Contact:");
                showContact(contacts, 0); // Call the new showContact
            } else {
                console.log("There are no contacts in the list.");
            }
            break;
        case "last":
            if (contacts.length > 0) {
                console.log("Last Contact:");
                showContact(contacts, contacts.length - 1); // Call the new showContact
            } else {
                console.log("There are no contacts in the list.");
            }
            break;
        case "new":
            let newName = readlineSync.question("Enter contact name: ");
            let newPhone = readlineSync.question("Enter contact phone number: ");
            let newEmail = readlineSync.question("Enter contact email: ");
            addNewContact(contacts, newName, newPhone, newEmail); // Call the new addNewContact
        break;


        case "quit":
            console.log("Exiting the program.");
            break;
        case "all":
            showAllContacts(contacts);
            break;
        default:
            console.log("Invalid choice. Please enter 'first', 'last', 'all', 'new', or 'quit'");

    }


}

// Main loop for continuous user interaction
let running = true;
let choice;
while (running) {
    manageContacts();
    running = choice.toLowerCase() !== "quit";
}
