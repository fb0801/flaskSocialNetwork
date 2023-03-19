DROP Table if exists posts;

CREATE TABLE posts (
    id integer primary key autoincrement,
    uname text not null, 
    content text not null
);