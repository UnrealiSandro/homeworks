<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        .parent {
            font-size: 500px;
        }
        .child {
            width: 25%; /* 25% of the parent div (which will be 125px since 500px * 25% = 125px) */
        }
        .paragraph {
            font-size: 50%; /* 50% of the parent div */
        }
    </style>
</head>
<body>
    <div class="parent">
        <div class="child">
            <p class="paragraph">Text</p>
        </div>
    </div>
</body>
</html>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        .outer-div {
            width: 1000px;
            height: 700px;
            background-color: darkblue;
        }
        .inner-div {
            width: 50%;
            height: 50%;
            background-color: yellow;
        }
    </style>
</head>
<body>
    <div class="outer-div">
        <div class="inner-div"></div>
    </div>
</body>
</html>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        .outer-div {
            width: 1000px;
            height: 700px;
            background-color: black;
        }
        .inner-div {
            width: 25%;
            height: 25%;
            background-color: red;
        }
    </style>
</head>
<body>
    <div class="outer-div">
        <div class="inner-div"></div>
    </div>
</body>
</html>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        .outer-div {
            width: 1000px;
            height: 1000px;
        }
        .image {
            width: 12.5%; /* Half of half of half is 12.5% */
            height: 12.5%;
        }
    </style>
</head>
<body>
    <div class="outer-div">
        <img class="image" src="your-image.jpg" alt="Image">
    </div>
</body>
</html>
