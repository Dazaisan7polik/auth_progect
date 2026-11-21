create table if not exists users (
    id serial primary key,
    role varchar(50) not null,
    username varchar(50) unique not null, 
    password varchar(50) not null,
    name varchar(100) not null
);

-- тестовые юзеры

insert into users (role, username, password, name) values
('admin', 'admin1', 'admin123', 'Alesana'),
('manager', 'manager_chelsea', 'manager123', 'Chelsea'),
('user', 'just_user', 'user123', 'Justin');
