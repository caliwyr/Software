# Naming

## Create vs Add

https://ux.stackexchange.com/questions/43174/update-vs-modify-vs-change-create-vs-add-delete-vs-remove

What's best calling these things depends on:

Who is using the system;
what is the nature of the action really being performed;
what other actions may be performed.
The Programmers View
With relation to databases (and data-driven APIs) there's the famous CRUD operations, which stand for Create/Read/Update/Destroy.

In many programming languages you may first create a record, then add it to a container, then remove it from the container, then destroy or delete it.

Also, in programming, change denotes something that is yet to be persisted (saved to the database or file), while update denotes persisting the change. Modify is not common, but you do get 'modified records' as a flag for a non-persisted state (aka, 'dirty records').

Everyday Language
You can argue that people will agree on these definitions:

You create something from scratch. Like create a new report.
Once in existence, you add something to a container. Like adding a person to the managers group.

By modifying something you change its properties. Like modifying a design.

By updating something you change the data, but not the design. Like updating someone's phone number.
By changing something you replace one existing thing with another. Like changing your profile photo.

By removing something you take it out of a container. Like removing something from the fridge - the thing still exist.

By destroying something you do the opposite from creating - gone forever. Like destroying a toy.
By deleting something you wipe if off, so it is no longer retrievable. This is said with the obvious exception that nowadays people are accustomed to the 'undelete' feature. So somewhat of an ambiguity here, but it is a standard in interfaces to use the term for permanent delation.
My Recommendations
Prefer Add over Create unless there's a clear create-then-add mechanism. Although technically (and as you said) create means it never existed before, while programmers think about 'records' users think about the abstraction these stand for. While for you adding a person's record makes perfect sense, 'creating a person' or 'creating a task' is less intuitive than 'adding a person' (to the system) or 'adding a task' (to the task list). Obviously, if your users are IT professionals and fluent with what a database and records are, prefer create over add.
If persistance is involved, prefer update over change. Having said that, users are accustomed to 'save changes'. Don't use modify.
Prefer Remove for non-permanent removal, and Delete for permanent removal.
