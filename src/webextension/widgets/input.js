/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

import PropTypes from "prop-types";
import React from "react";

import styles from "./input.css";

export default function Input({className, ...props}) {
  let finalClassName = `${styles.input} ${className || ""}`.trimRight();
  return (
    <span className="browser-style">
      <input className={finalClassName} {...props}/>
    </span>
  );
}

Input.propTypes = {
  className: PropTypes.string,
};
