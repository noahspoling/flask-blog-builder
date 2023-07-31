import {html} from "../../packages/arrow.js"

const contactForm = html`
    <form>
        <div class="formGroup">
            <label for="CurrentPassword">Current Password</label>
            <input type="password" name="CurrentPassword" id="inputCurrentPassword"/>
        </div>
        <div class="formGroup">
            <label for="NewPassword">New Password</label>
            <input type="password" name="NewPassword" id="inputNewPassword">
        </div>
        <div class="formGroup">
            <label for="VerifyNewPassword">Verify New Password</label>
            <input type="password" name="VerifyNewPassword" id="inputVerifyNewPassword">
        </div>
        <div class="formGroup">
            <button class="formButton" type="submit">Send</button>
            <button class="formButton" type="reset">Clear</button>
        </div>
    </form>
`

export default contactForm;