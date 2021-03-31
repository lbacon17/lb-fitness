// gets each rating star
var one = document.getElementById("first-{{ video.id }}");
var two = document.getElementById("second-{{ video.id }}");
var three = document.getElementById("third-{{ video.id }}");
var four = document.getElementById("fourth-{{ video.id }}");
var five = document.getElementById("fifth-{{ video.id }}");

var ratingForm = document.querySelector('.rating-form');
var ratingConfirmation = document.getElementById('rating-confirmation');
var csrfToken = document.getElementsByName('csrfmiddlewaretoken');

// adds and removes checked class to/from rating stars
function handleStarSelect(size) {
    var childElements = ratingForm.children;
    for (let i = 0; i < childElements.length; i++) {
        if (i <= size) {
            childElements[i].classList.add('checked');
        } else {
            childElements[i].classList.remove('checked');
        }
    }            
}

// determines how many stars to check
function handleSelect(selection) {
    switch(selection){
        case 'first-{{ video.id }}': {
            handleStarSelect(1);
            return;
        }
        case 'second-{{ video.id }}': {
            handleStarSelect(2);
            return;
        }
        case 'third-{{ video.id }}': {
            handleStarSelect(3);
            return;
        }
        case 'fourth-{{ video.id }}': {
            handleStarSelect(4);
            return;
        }
        case 'fifth-{{ video.id }}': {
            handleStarSelect(5);
            return;
        }
        default: {
            handleStarSelect(0);
        }
    }
}

function getNumericValue(stringValue) {
    let numericValue;
    if (stringValue === 'first-{{ video.id }}') {
        numericValue = 1;
    } else if (stringValue === 'second-{{ video.id }}') {
        numericValue = 2;
    } else if (stringValue === 'third-{{ video.id }}') {
        numericValue = 3;
    } else if (stringValue === 'fourth-{{ video.id }}') {
        numericValue = 4;
    } else if (stringValue === 'fifth-{{ video.id }}') {
        numericValue = 5;
    } else {
        numericValue = 0;
    }
    return numericValue;
}

if (one) {
    const ratingStars = [one, two, three, four, five];

    ratingStars.forEach(item=> item.addEventListener('mouseover', (event)=>{
        handleSelect(event.target.id);
    }));

    ratingStars.forEach(item=> item.addEventListener('click', (event)=>{
        const val = event.target.id;

        let isSubmit = false;
        ratingForm.addEventListener('submit', e=>{
            e.preventDefault();
            if (isSubmit) {
                return;
            }
            isSubmit = true;
            const videoId = e.target.id;
            const val_num = getNumericValue(val);
            $.ajax({
                type: 'POST',
                url: '/videos/rate_video/',
                data: {
                    'csrfmiddlewaretoken': csrfToken[0].value,
                    'video_id': videoId,
                    'val': val_num
                },
                success: function(response) {
                    ratingConfirmation.innerHTML = `<h6 class="text-success">Successfully rated video as ${response.rating} stars.</h6>`;
                },
                error: function(error) {
                    ratingConfirmation.innerHTML = `<h6 class="text-danger">An error occurred. Please try again</h6>`;
                }
            });
        });
    }));
}