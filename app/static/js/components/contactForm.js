import {html} from "../packages/arrow.js"




const contactForm = html`
    <form>
        <div class="formGroup">
            <label for="name">Name</label>
            <input type="text" name="Name" id="inputName"/>
        </div>
        <div class="formGroup">
            <label for="email">Email</label>
            <input type="email" name="email" id="inputEmail">
        </div>
        <div class="formGroup">
            <label for="comment">Comment</label>
            <textarea name="comment" id="inputComment" cols="30" rows="5"></textarea>
        </div>
        <div class="formGroup">
            <button type="submit">Send</button>
            <button type="reset">Clear</button>
        </div>
    </form>
`

export default contactForm;