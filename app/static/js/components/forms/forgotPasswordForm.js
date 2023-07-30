import {html} from "../../packages/arrow.js"

const contactForm = html`
    <form>
        <div class="formGroup">
            <label for="Email">Email</label>
            <input type="password" name="VerifyNewPassword" id="inputVerifyNewPassword">
        </div>
        <div class="formGroup">
            <button type="submit">Send</button>
            <button type="reset">Clear</button>
        </div>
    </form>
`

export default contactForm;