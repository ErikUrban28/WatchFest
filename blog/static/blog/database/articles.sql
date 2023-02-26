create table articles
(
    id    int auto_increment
        primary key,
    title text not null,
    text  text not null,
    img   text null
);

INSERT INTO Watchfest_DB.articles (id, title, text, img) VALUES (1, 'Game of Thrones: House of Dragon', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec iaculis blandit lacus vel mattis. Aliquam vitae dolor magna. Interdum et malesuada fames ac ante ipsum primis in faucibus. Integer rhoncus faucibus elementum. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Pellentesque sed dapibus augue. Nam tincidunt consequat risus et commodo. Fusce at eros eu mi porta congue. Quisque luctus lobortis pharetra.                 ', 'blog/images/House_of_dragon.jpg');
INSERT INTO Watchfest_DB.articles (id, title, text, img) VALUES (4, 'The Lord of the Rings: The Rings of Power ', '            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusantium alias cumque ea nihil nisi perferendis quia? Ducimus, eos, magnam molestiae natus nemo neque perspiciatis quasi rerum saepe sed ut veniam? Culpa cupiditate eligendi quam. Dolorem eveniet iure magni neque numquam optio quae quia reprehenderit tempora tenetur. Accusamus minima minus officia placeat repellendus repudiandae soluta, ullam! Blanditiis consectetur magnam quaerat tenetur. Accusamus, at atque beatae consectetur cumque delectus deserunt dicta eius eos eveniet excepturi ipsa iste, iusto laudantium modi, molestiae mollitia nam nobis perspiciatis possimus p raesentium ratione recusandae similique temporibus vero! Aperiam at consectetur debit is deserunt dolor ducimus, eligendi error facilis, illum ipsam ipsum itaque iure maxime neque nisi, nobis nostrum perferendis quas quia quis reiciendis rerum suscipit tempora totam veritatisa.         ', 'blog/images/LOTR.jpg');
