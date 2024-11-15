// SPDX-License-Identifier: Apache-2.0
pragma solidity ^0.8.0;

import {IERC20} from "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title IPriceOracle interface
 * @dev Interface that returns the price of tokens
 * @author Bang
 */
interface IPriceOracle {
  /**
   * @dev Returns the amount of units of tokenOut that should be received for a uint of tokenIn
   *
   * Requirements:
   * - The underlying oracle(s) are functional. It NEVER returns zero.
   *
   * @return Returns the amount of units of tokenOut that should be received for a uint of tokenIn
   */
  function getCurrentPrice(IERC20 tokenIn, IERC20 tokenOut) external view returns (uint256);
}
